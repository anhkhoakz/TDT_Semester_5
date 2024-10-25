import java.awt.Desktop;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.OutputStream;
import java.net.HttpURLConnection;
import java.net.URL;
import java.util.Properties;
import java.util.Scanner;

public class oath_demo {

    public static void main(String[] args) {
        try {
            Properties env = loadEnvVariables();
            String clientId = env.getProperty("GH_CLIENT_ID");
            String clientSecret = env.getProperty("GH_CLIENT_SECRET");

            String authCode = getAuthCode(clientId);
            String accessToken = getAccessToken(clientId, clientSecret, authCode);
            String userData = getUserData(accessToken);

            System.out.println(userData);

        } catch (Exception e) {
            e.printStackTrace();
        }
    }

    private static Properties loadEnvVariables() throws Exception {
        Properties env = new Properties();
        env.load(oath_demo.class.getResourceAsStream("/.env"));
        return env;
    }

    private static String getAuthCode(String clientId) throws Exception {
        String authEndpoint = "https://github.com/login/oauth/authorize?response_type=code&client_id=" + clientId;
        if (Desktop.isDesktopSupported()) {
            Desktop.getDesktop().browse(new URL(authEndpoint).toURI());
        }
        System.out.println("Open this link in your browser: " + authEndpoint);
        Scanner scanner = new Scanner(System.in);
        System.out.print("Enter the auth code: ");
        return scanner.nextLine();
    }

    private static String getAccessToken(String clientId, String clientSecret, String authCode) throws Exception {
        String tokenEndpoint = "https://github.com/login/oauth/access_token";
        URL url = new URL(tokenEndpoint);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("POST");
        conn.setRequestProperty("Content-Type", "application/x-www-form-urlencoded");
        conn.setDoOutput(true);

        String data = "client_id=" + clientId + "&client_secret=" + clientSecret + "&code=" + authCode;
        try (OutputStream os = conn.getOutputStream()) {
            os.write(data.getBytes());
            os.flush();
        }

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder content = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();
        conn.disconnect();

        String response = content.toString();
        String accessToken = response.split("&")[0].split("=")[1];
        return accessToken;
    }

    private static String getUserData(String accessToken) throws Exception {
        String userEndpoint = "https://api.github.com/user";
        URL url = new URL(userEndpoint);
        HttpURLConnection conn = (HttpURLConnection) url.openConnection();
        conn.setRequestMethod("GET");
        conn.setRequestProperty("Authorization", "token " + accessToken);

        BufferedReader in = new BufferedReader(new InputStreamReader(conn.getInputStream()));
        String inputLine;
        StringBuilder content = new StringBuilder();
        while ((inputLine = in.readLine()) != null) {
            content.append(inputLine);
        }
        in.close();
        conn.disconnect();

        return content.toString();
    }
}

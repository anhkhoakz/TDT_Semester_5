using Microsoft.Extensions.Options;
using Microsoft.OpenApi.Models;
using Newtonsoft.Json;
using RestSharp;
using System.Security.Cryptography;
using System.Text;
using TicketHub.Models;
using TicketHub.Service.Momo.Models;

namespace TicketHub.Service.Momo
{
    public class MomoService : IMomoService
    {
        private readonly IOptions<MomoOptionModel> _options;
        private readonly MomoConfig momoConfig;
        private readonly HttpClient _httpClient;

        public MomoService(IOptions<MomoOptionModel> options, IOptions<MomoConfig> momoConfig, IHttpClientFactory httpClientFactory)
        {
            _options = options;
            this.momoConfig = momoConfig.Value;
            _httpClient = httpClientFactory.CreateClient();
        }

        public async Task<MomoCreatePaymentResponseModel> CreatePaymentAsync(OrderInfoModel model)
        {
            model.OrderId = DateTime.UtcNow.Ticks.ToString();
            model.OrderInfo = "Khách hàng: " + model.FullName + ". Nội dung: " + model.OrderInfo;

            var result = new MomoCreatePaymentResponseModel();


            var momoOneTimePayRequest = new MomoOneTimePaymentRequest(momoConfig.PartnerCode,
                                model.OrderId ?? string.Empty, (long)model.Amount!, model.OrderId ?? string.Empty,
                                model.OrderInfo?? string.Empty, momoConfig.ReturnUrl, momoConfig.IpnUrl, "captureWallet",
                                string.Empty);

            if (momoOneTimePayRequest == null)
                return result;


            momoOneTimePayRequest.MakeSignature(momoConfig.AccessKey, momoConfig.SecretKey);

            (bool createMomoLinkResult, string? createMessage) = momoOneTimePayRequest.GetLink(momoConfig.PaymentUrl);
            if (createMomoLinkResult)
                result.payUrl = createMessage;
            
            else
                result.message = createMessage;

            return result;
        }



        public MomoExecuteResponseModel PaymentExecuteAsync(IQueryCollection collection)
        {
            var amount = collection.First(s => s.Key == "amount").Value;
            var orderInfo = collection.First(s => s.Key == "orderInfo").Value;
            var orderId = collection.First(s => s.Key == "orderId").Value;
            return new MomoExecuteResponseModel()
            {
                Amount = amount,
                OrderId = orderId,
                OrderInfo = orderInfo
            };
        }

        private string ComputeHmacSha256(string key, string inputData)
        {
            byte[] keyByte = Encoding.UTF8.GetBytes(key);
            byte[] messageBytes = Encoding.UTF8.GetBytes(inputData);
            using (var hmacsha256 = new HMACSHA256(keyByte))
            {
                byte[] hashmessage = hmacsha256.ComputeHash(messageBytes);
                string hex = BitConverter.ToString(hashmessage);
                hex = hex.Replace("-", "").ToLower();
                return hex;
            }
        }
    }
}

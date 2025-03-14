﻿using Newtonsoft.Json.Serialization;
using Newtonsoft.Json;
using System.Text;
using TicketHub.Helper;
using System.Net.Http;

namespace TicketHub.Service.Momo.Models
{
    public class MomoOneTimePaymentRequest
    {
        public string partnerCode { get; set; } = string.Empty;
        public string requestId { get; set; } = string.Empty;
        public long amount { get; set; }
        public string orderId { get; set; } = string.Empty;
        public string orderInfo { get; set; } = string.Empty;
        public string redirectUrl { get; set; } = string.Empty;
        public string ipnUrl { get; set; } = string.Empty;
        public string requestType { get; set; } = string.Empty;
        public string extraData { get; set; } = string.Empty;
        public string lang { get; set; } = string.Empty;
        public string signature { get; set; } = string.Empty;

        public MomoOneTimePaymentRequest(string partnerCode, string requestId,
            long amount, string orderId, string orderInfo, string redirectUrl,
            string ipnUrl, string requestType, string extraData, string lang = "vi")
        {
            this.partnerCode = partnerCode;
            this.requestId = requestId;
            this.amount = amount;
            this.orderId = orderId;
            this.orderInfo = orderInfo;
            this.redirectUrl = redirectUrl;
            this.ipnUrl = ipnUrl;
            this.requestType = requestType;
            this.extraData = extraData;
            this.lang = lang;
        }
        




        public void MakeSignature(string accessKey, string secretKey)
        {
            var rawHash = "accessKey=" + accessKey +
                "&amount=" + this.amount +
                "&extraData=" + this.extraData +
                "&ipnUrl=" + this.ipnUrl +
                "&orderId=" + this.orderId +
                "&orderInfo=" + this.orderInfo +
                "&partnerCode=" + this.partnerCode +
                "&redirectUrl=" + this.redirectUrl +
                "&requestId=" + this.requestId +
                "&requestType=" + this.requestType;
            this.signature = HashHelper.HmacSHA256(rawHash, secretKey);
        }



        public (bool, string?) GetLink(string paymentUrl)
        {
            using HttpClient client = new HttpClient();
            var requestData = JsonConvert.SerializeObject(this, new JsonSerializerSettings()
            {
                ContractResolver = new CamelCasePropertyNamesContractResolver(),
                Formatting = Formatting.Indented,
            });
            var requestContent = new StringContent(requestData, Encoding.UTF8,
                "application/json");

            var createPaymentLinkRes = client.PostAsync(paymentUrl, requestContent).Result;

            //var createPaymentLinkRes = await _httpClient.PostAsync(paymentUrl, requestContent);

            var responseContent = createPaymentLinkRes.Content.ReadAsStringAsync().Result;
            Console.WriteLine("Raw API Response: " + responseContent);



            if (createPaymentLinkRes.IsSuccessStatusCode)
            {
                var responseData = JsonConvert.DeserializeObject<MomoCreatePaymentResponseModel>(responseContent);
                
                if (responseData?.resultCode == "0")
                {
                    return (true, responseData.payUrl);
                }
                else if (responseData == null)
                {
                    Console.WriteLine("Failed to deserialize API response.");
                    return (false, "Invalid response from payment service.");
                }

                else
                {
                    return (false, responseData?.message);
                }

            }
            else
            {
                return (false, createPaymentLinkRes.ReasonPhrase);
            }
        }
    }
}

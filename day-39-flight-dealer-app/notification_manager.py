from twilio.rest import Client


class NotificationManager:
    ACC_SID = "AC67d6343e52156c4c0dc88ca85ca852ed"
    AUTH_TOKEN = "d6eccdd27d18e311b8e6852b0e43c1cf"
    PHONE_FROM = "+17164669165"
    PHONE_TO = "+77024528029"

    def send_message(self, price, dep_city, dep_city_code, arr_city, arr_city_code, outbound, inbound):
        client = Client(self.ACC_SID, self.AUTH_TOKEN)

        message = client.messages.create(
            body=f"Low price Alert!\nOnly £{price} to fly from {dep_city}-{dep_city_code} to "
                 f"{arr_city}-{arr_city_code}, from {outbound} to {inbound}",
            from_=self.PHONE_FROM,
            to=self.PHONE_TO
        )


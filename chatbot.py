import json

class CollegeChatbot:
    def __init__(self, data_path="data.json"):
        with open(data_path, "r") as file:
            self.data = json.load(file)

    def get_response(self, user_input):
        user_input = user_input.lower()

        # Courses
        if "course" in user_input or "program" in user_input:
            return "Our available courses:\n- " + "\n- ".join(self.data["courses"])

        # Fees
        if "fee" in user_input or "fees" in user_input:
            return "Fee structure:\n" + "\n".join([f"{k}: {v}" for k, v in self.data["fees"].items()])

        # Admission
        if "admission" in user_input:
            return "Admission Process:\n" + self.data["admission_process"]

        # Contact
        if "contact" in user_input or "reach" in user_input:
            return f"Contact us at:\nEmail: {self.data['contact']['email']}\nPhone: {self.data['contact']['phone']}"

        # Default
        return "Sorry, I didn't understand that. Please ask about courses, fees, admission, or contact."

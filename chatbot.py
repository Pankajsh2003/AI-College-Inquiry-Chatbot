import json

class CollegeChatbot:
    def __init__(self, data_path="data.json"):
        with open(data_path, "r") as file:
            self.data = json.load(file)

    def get_response(self, user_input):
        text = user_input.lower()

        # ---- COURSES ----
        course_keywords = ["course", "courses", "program", "branch", "study", "offer"]
        if any(word in text for word in course_keywords):
            return "Available Courses:\n- " + "\n- ".join(self.data["courses"])

        # ---- FEES ----
        fee_keywords = ["fee", "fees", "cost", "price", "structure", "pay"]
        if any(word in text for word in fee_keywords):
            fees = "\n".join([f"{k}: {v}" for k, v in self.data["fees"].items()])
            return "Fee Structure:\n" + fees

        # ---- ADMISSION ----
        admission_keywords = ["admission", "apply", "process", "entrance", "form"]
        if any(word in text for word in admission_keywords):
            return f"Admission Process:\n{self.data['admission_process']}"

        # ---- CONTACT ----
        contact_keywords = ["contact", "call", "email", "phone", "reach", "support"]
        if any(word in text for word in contact_keywords):
            c = self.data["contact"]
            return f"Contact:\n📧 {c['email']}\n📞 {c['phone']}"

        # ---- DEFAULT ----
        return (
            "Sorry, I couldn't understand your question.\n\n"
            "You can ask me about:\n"
            "- Courses\n"
            "- Fees\n"
            "- Admission Process\n"
            "- Contact Information"
        )

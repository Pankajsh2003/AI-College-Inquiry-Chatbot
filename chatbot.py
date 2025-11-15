import json

class CollegeChatbot:
    def __init__(self, data_path="data.json"):
        with open(data_path, "r") as file:
            self.data = json.load(file)

    def get_response(self, text):
        text = text.lower()

        # ----- COURSES -----
        if any(word in text for word in ["course", "courses", "program", "branch"]):
            return "Available Courses:\n- " + "\n- ".join(self.data["courses"])

        # ----- FEES -----
        if any(word in text for word in ["fee", "fees", "cost", "price"]):
            fees = "\n".join([f"{k}: {v}" for k, v in self.data["fees"].items()])
            return "Fee Structure:\n" + fees

        # ----- ADMISSION -----
        if any(word in text for word in ["admission", "apply", "process", "entrance"]):
            return "Admission Process:\n" + self.data["admission_process"]

        # ----- CONTACT -----
        if any(word in text for word in ["contact", "email", "phone", "call"]):
            c = self.data["contact"]
            return f"Contact Details:\nEmail: {c['email']}\nPhone: {c['phone']}"

        # ----- PLACEMENTS -----
        placement_keywords = ["placement", "placements", "job", "campus", "company", "criteria"]
        if any(word in text for word in placement_keywords):
            p = self.data["placements"]
            return (
                "**Placement Details:**\n\n"
                f"📌 **Criteria**: {p['criteria']}\n"
                f"📌 **Companies**: {', '.join(p['companies'])}\n"
                f"📌 **Stats**: {p['stats']}"
            )

        # ----- DEFAULT -----
        return (
            "Sorry, I couldn't understand your question.\n\n"
            "You can ask about:\n"
            "- Courses\n"
            "- Fees\n"
            "- Admission\n"
            "- Contact\n"
            "- Placements"
        )

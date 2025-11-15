import json

class CollegeChatbot:
    def __init__(self, data_path="data.json"):
        with open(data_path, "r") as file:
            self.data = json.load(file)

    def get_response(self, text):
        text = text.lower()

        # ----- OVERVIEW -----
        if any(word in text for word in ["about", "overview", "info", "information", "details", "gitam kya"]):
            return self.data["overview"]

        # ----- COURSES -----
        course_keywords = ["course", "courses", "program", "branch", "offer", "subjects", "streams"]
        if any(word in text for word in course_keywords):
            return "Courses offered:\n- " + "\n- ".join(self.data["courses"])

        # ----- FEES -----
        fee_keywords = ["fee", "fees", "cost", "price", "structure", "charges", "tuition"]
        if any(word in text for word in fee_keywords):
            fees = "\n".join([f"{k}: {v}" for k, v in self.data["fees"].items()])
            return "Fee Structure:\n" + fees

        # ----- ADMISSION -----
        admission_keywords = ["admission", "apply", "process", "entrance", "gat", "exam", "eligibility"]
        if any(word in text for word in admission_keywords):
            return "Admission Process:\n" + self.data["admission_process"]

        # ----- PLACEMENTS -----
        placement_keywords = ["placement", "placements", "job", "package", "salary", "company", "companies", "campus"]
        if any(word in text for word in placement_keywords):
            p = self.data["placements"]
            return (
                "**Placement Details:**\n\n"
                f"📌 Criteria: {p['criteria']}\n"
                f"📌 Companies: {', '.join(p['companies'])}\n"
                f"📌 Stats: {p['stats']}"
            )

        # ----- HOSTEL -----
        hostel_keywords = ["hostel", "room", "stay", "ac", "non ac", "mess", "canteen", "wifi", "warden"]
        if any(word in text for word in hostel_keywords):
            h = self.data["hostel"]
            return (
                "**Hostel Details:**\n"
                f"- Rooms: {h['rooms']}\n"
                f"- AC: {h['ac']}\n"
                f"- WiFi: {h['wifi']}\n"
                f"- Mess: {h['mess']}\n"
                f"- Security: {h['security']}\n"
                f"- Fees: {h['fees']}"
            )

        # ----- FACILITIES -----
        facility_keywords = ["facility", "facilities", "infrastructure", "campus", "building", "features"]
        if any(word in text for word in facility_keywords):
            return "Facilities:\n- " + "\n- ".join(self.data["facilities"])

        # ----- CONTACT -----
        contact_keywords = ["contact", "email", "phone", "call", "number", "address", "location"]
        if any(word in text for word in contact_keywords):
            c = self.data["contact"]
            return (
                "Contact Details:\n"
                f"📧 Email: {c['email']}\n"
                f"📞 Phone: {c['phone']}\n"
                f"📍 Address: {c['address']}"
            )

        # ----- DEFAULT -----
        return (
            "Sorry, I couldn't understand your question.\n\n"
            "You can ask about:\n"
            "- Courses\n"
            "- Fees\n"
            "- Admission\n"
            "- Placements\n"
            "- Hostel\n"
            "- Facilities\n"
            "- Overview\n"
            "- Contact"
        )

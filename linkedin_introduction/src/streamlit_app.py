import streamlit as st
from dataclasses import dataclass, field
from typing import List

# ---------------- Developer DataClass ----------------
@dataclass
class Developer:
    first_name: str
    last_name: str
    skills: List[str] = field(default_factory=list)
    motto: str = "Code with clarity, deploy with confidence!"

    def introduce(self) -> str:
        return (
            f"👨‍💻 **My name is {self.first_name} {self.last_name}**\n\n"
            f"🛠️ **Core Skills:** {', '.join(self.skills)}\n\n"
            f"✨ *Fun Fact:* Code never sleeps, and neither do I (debugging at 2AM)!\n\n"
            f"💡 **Motto:** _{self.motto}_"
        )

# ---------------- Areas DataClass ----------------
@dataclass
class Areas:
    selective_areas: List[str] = field(default_factory=list)

    def random_skill(self, user_area: str) -> str:
        if user_area == "Data":
            return "🔥 Highlighted Skill: Data Structures & Algorithms, Python, SQL | Database, Crawling"
        elif user_area in ["Web Development", "Software Development"]:
            return "🔥 Highlighted Skill: Web Development, Software Development"
        elif user_area == "Business Development":
            return (
                "🔥 Highlighted Skill: Business Process Automation, Project Management, "
                "Reporting & Analysis, Knowledge Management, Workflows Monitoring, Creative Problem Solving"
            )
        else:
            return "❌ No skills available for this area."

# ---------------- Streamlit UI ----------------
def main():
    st.set_page_config(page_title="Developer CV", page_icon="💻", layout="centered")

    # --- Developer Info ---
    me = Developer(
        first_name="Mahdis",
        last_name="Ahmadi",
        skills=[
            "Python",
            "SQL | Databases",
            "Data Structures & Algorithms",
            "Docker",
            "Software Development",
            "Web Development",
            "Crawling",
        ],
    )

    st.title("💻 Interactive Developer CV")
    st.markdown(me.introduce())

    st.divider()
    st.subheader("🎯 Explore My Expertise Areas")

    # --- Area Selection ---
    areas = ["Data", "Web Development", "Software Development", "Business Development"]
    selected_area = st.selectbox("Select an area to view my highlighted skills:", areas)

    area_instance = Areas(selective_areas=areas)
    st.success(area_instance.random_skill(selected_area))

    st.divider()
    st.caption("Created with ❤️ by Mahdis Ahmadi")

if __name__ == "__main__":
    main()


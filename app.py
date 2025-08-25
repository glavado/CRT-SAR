
import streamlit as st

st.set_page_config(page_title="Subject Access Request Decision Tree", layout="wide")

st.title("🎓 Subject Access Request Decision Tree")
st.markdown("Use this interactive tool to determine how to handle SARs based on the process flow.")

# Step 1: Ministry Case Check
st.header("Step 1: Ministry Case Check")
ministry_case = st.radio("Is this a Ministry case?", ["Yes", "No"])

if ministry_case == "Yes":
    st.info("Refer to the card ‘Ministry SARs’.")
else:
    # Step 2: CMR Request Check
    st.header("Step 2: CMR Request Check")
    cmr_request = st.radio("Is this a CMR request from J24 onward?", ["Yes", "No"])
    if cmr_request == "Yes":
        st.success("Refer back to the school. Use Trello response: 'Quicker to contact school to receive component marks information (or for M25 script / item level marks)'.")
    else:
        # Step 3: ATS June 2025 Eligibility
        st.header("Step 3: ATS June 2025 Eligibility")
        country = st.selectbox("Select the candidate's country:", ["China", "Cuba", "Iran", "Mauritius", "Maldives", "Other"])
        if country in ["China", "Cuba", "Iran", "Mauritius", "Maldives"]:
            st.warning("ATS June 2025 service is not available for this country.")
            st.info("Access the script via RM Assessor. [Pending confirmation from Ellie]")
        else:
            st.success("ATS June 2025 service is available. Refer back to the centre for component marks, item level data, or copies of scripts.")

        # Step 4: MCQ Requests
        st.header("Step 4: MCQ Requests")
        mcq_request = st.radio("Is this a request for MCQ (Multiple Choice Question Paper)?", ["Yes", "No"])
        if mcq_request == "Yes":
            st.success("Send to CI Assessment Data and Analytics: CIAssessmentDataAndAnalytics@cambridge.org (keep ticket in view).")

        # Step 5: Historic Requests
        st.header("Step 5: Historic Requests")
        historic_type = st.selectbox("Select the type of historic request:", [
            "PK learner component marks (Nov21–Mar24)",
            "Copy of script (≤11 months old)",
            "Copy of script (11–18 months old)",
            "Copy of script (>18 months old)",
            "Other country component marks (pre-J25)",
            "PK component marks (pre-N21)",
            "Item level marks (any series)",
            "MCQ request (not in ATS)"
        ])

        if historic_type == "PK learner component marks (Nov21–Mar24)":
            st.info("Refer to the recording and process document.")
        elif historic_type == "Copy of script (≤11 months old)":
            st.success("CRT can access via RM Assessor.")
        elif historic_type == "Copy of script (11–18 months old)":
            st.warning("Contact Leah Dark to confirm if we still hold the script or if Archives do.")
        elif historic_type == "Copy of script (>18 months old)":
            st.error("We do not hold the script. It has been destroyed.")
        else:
            st.success("Send to CI Assessment Data and Analytics: CIAssessmentDataAndAnalytics@cambridge.org (keep ticket in view).")

import streamlit as st

st.title("Subject Access Request (SAR) Process Guide")

# Initial Checks
st.header("Initial Checks")
previous_request = st.radio("Has this candidate contacted us before?", ["Yes", "No"])
if previous_request == "Yes":
    st.info("Use Macro: 'Multiple requests from the same person'")

id_received = st.radio("Has the candidate provided ID?", ["Yes", "No"])
if id_received == "No":
    st.warning("Use Macro: 'Provide ID'")

ministry_case = st.radio("Is this a Ministry country?", ["Yes", "No"])
if ministry_case == "Yes":
    st.info("Refer to the card ‘Ministry SARs’.")

# CMR and Item-Level Mark Requests
st.header("Step 2: CMR and Item-Level Mark Requests")
cmr_request = st.radio("Is this a CMR request from J24 onward?", ["Yes", "No"])
item_level_request = st.radio("Is this an item-level mark request from J25 onward?", ["Yes", "No"])

if cmr_request == "Yes" and item_level_request == "Yes":
    st.success("Use Macro: 'Response: J25 onward - CMR and Item level marks request'")
elif cmr_request == "Yes":
    st.success("Use Macro: 'Response: J24 onwards - CMR request'")
elif item_level_request == "Yes":
    st.success("Use Macro: 'Response: J25 onward - item level marks request'")

# ATS Service Eligibility
st.header("Step 3: ATS June 2025 Eligibility")
country = st.selectbox("Select the candidate's country:", ["China", "Cuba", "Iran", "Mauritius", "Maldives", "Other"])
bc_private_candidate = st.radio("Is this a British Council private candidate?", ["Yes", "No"])

if country in ["China", "Cuba", "Iran", "Mauritius", "Maldives"]:
    st.warning("ATS June 2025 service is not available for this country.")
elif bc_private_candidate == "Yes":
    st.warning("Use Macro: 'Response: Unable to access ATS as a PK private candidate'")
else:
    st.success("ATS June 2025 service is available.")

# COS Requests
st.header("Step 4: Copy of Script (COS) Requests")
cos_type = st.selectbox("Type of COS request:", ["COS only", "COS + annotations"])

if cos_type == "COS only":
    st.success("Use Macro: 'Request for copy of script under SAR'")
elif cos_type == "COS + annotations":
    st.success("Use Macro: 'Script request for annotations under SAR' and provide via RM Assessor")

# MCQ Requests
st.header("Step 5: MCQ Requests")
mcq_request = st.radio("Is this a request for MCQ (Multiple Choice Question Paper)?", ["Yes", "No"])
if mcq_request == "Yes":
    st.success("Send to ADA: CIAssessmentDataAndAnalytics@cambridge.org. Use Macro: 'Subject Access Request: Template to raise to ASQ'")

# Historic Requests
st.header("Step 6: Historic Requests")
historic_type = st.selectbox("Select the type of historic request:", [
    "PK learner component marks (Nov21–Mar24)",
    "Copy of script (≤11 months old)",
    "Copy of script (11–18 months old)",
    "Copy of script (>18 months old)",
    "Other country component marks (pre-J24)",
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
    st.success("Send to ADA: CIAssessmentDataAndAnalytics@cambridge.org. Use Macro: 'Subject Access Request - Template to raise requests (ADA)'")

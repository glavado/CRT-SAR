import streamlit as st

st.title("SAR Process Guide")

# Initial Checks
st.header("Initial Checks")
with st.expander("Initial Checks"):
    previous_request = st.radio("Has this candidate contacted us before?", ["Yes", "No"])
    if previous_request == "Yes":
        st.warning("Use Macro: 'Multiple requests from the same person'")
    if previous_request == "No":
        st.info("Proceed with request.") 

    id_received = st.radio("Has the candidate provided appropriate ID?", ["Yes", "No"])
    if id_received == "No":
        st.error("Use Macro: 'Provide ID'")
    if id_received == "Yes":
        st.info("Proceed with request.") 

    ministry_case = st.radio("Is this a Ministry country?", ["Yes", "No"])
    if ministry_case == "Yes":
        st.warning("Refer to the card ‘Ministry SARs’.")
    if ministry_case == "No":
        st.info("Proceed with request.") 

# Refer to School (J24+ CMR & J25 Item-Level)
st.header("Refer to School (J24+ CMR & J25 Item-Level)")
with st.expander("Refer to School (J24+ CMR & J25 Item-Level)"):

    cmr_request = st.radio("Is this a CMR request from J24 onward?", ["", "Yes", "No"])
    item_level_request = st.radio("Is this an item-level mark request from J25 onward?", ["", "Yes", "No"])

    if cmr_request == "Yes" and item_level_request == "Yes":
        st.success("Use Macro: 'Response: J25 onward - CMR and Item level marks request'")
    elif cmr_request == "Yes":
        st.success("Component marks info has been released to all schools. Use Macro: 'Response: J24 onwards - CMR request'")
    elif item_level_request == "Yes":
        st.success("ATS service includes item-level marks. Use Macro: 'Response: J25 onward - item level marks request' (except for non-ATS eligible.)")

# J25 - Access to Scripts / Copy of Script
st.header("J25 - Access to Scripts / Copy of Script")
with st.expander("J25 - Access to Scripts / Copy of Script"):

    # ATS Service Eligibility
    st.markdown("### ATS June 2025 Eligibility")
    country = st.selectbox("Select the candidate's country:", ["Select a country", "China", "Cuba", "Iran", "Mauritius", "Maldives", "Other"])
    bc_private_candidate = st.radio("Is this a British Council PK private candidate?", ["", "Yes", "No"])

    if country in ["China", "Cuba", "Iran", "Mauritius", "Maldives"]:
        st.warning("ATS June 2025 service is not available for this country.")
    elif bc_private_candidate == "Yes":
        st.error("ATS not available. For ATS-related concern, use Macro: 'Response: Unable to access ATS as a PK private candidate'")
    elif country != "" and bc_private_candidate != "":
        st.success("ATS June 2025 service is available.")

    # COS Requests
    st.markdown("### Copy of Script (COS) Requests")
    cos_type = st.selectbox("Type of COS request:", ["Select", "COS only", "COS + annotations for J25"])

    if cos_type == "COS only":
        st.success("Use Macro: 'Request for copy of script under SAR'")
    elif cos_type == "COS + annotations for J25":
        st.success("Add to ‘COS for J25’ list while we wait for instructions")

    # MCQ Requests
    st.markdown("### MCQ Requests")
    mcq_request = st.radio("Is this a request for MCQ item-level marks?", ["Yes", "No"])
    if mcq_request == "Yes":
        st.success("MCQ item-level marks are not available in ATS. Send to ADA: CIAssessmentDataAndAnalytics@cambridge.org. Use Macro: 'Subject Access Request: Template to raise to ASQ'")

# Historic Requests
st.header("Historic Requests")
with st.expander("Historic Requests"):
    historic_type = st.selectbox("Select the type of historic request:", ["Select",
        "PK CMR (Nov21–Mar24)",
        "PK CMR (pre-N21)",
        "Other country/Non-PK CMR (pre-J24)",                                                                 
        "Copy of script (≤11 months old)",
        "Copy of script (11–18 months old)",
        "Copy of script (>18 months old)",
        "Item level marks (any series)",
        "MCQ request (not in ATS)"
    ])
    
    if historic_type == "PK CMR (Nov21–Mar24)":
        st.info("Refer to the recording and process document.")
    elif historic_type == "Copy of script (≤11 months old)":
        st.success("CRT can access via RM Assessor.")
    elif historic_type == "Copy of script (11–18 months old)":
        st.warning("Contact Leah Dark to confirm if we still hold the script or if Archives do.")
    elif historic_type == "Copy of script (>18 months old)":
        st.error("We do not hold the script. It has been destroyed.")
    elif historic_type in [
        "Other country/Non-PK CMR (pre-J24)", 
        "PK CMR (pre-N21)",
        "Item level marks (any series)",
        "MCQ request (not in ATS)"
    ]: 
        st.success("Send to ADA: CIAssessmentDataAndAnalytics@cambridge.org. Use Macro: 'Subject Access Request - Template to raise requests (ADA)'")

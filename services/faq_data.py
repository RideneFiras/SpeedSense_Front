
faq_list = [
    {
        "question": "What is SpeedSens?",
        "answer": "SpeedSens is an AI-powered tool designed to help telecom operators predict 5G throughput. By learning from real-world network and environmental data, it delivers smart, actionable insights to improve Quality of Service before issues arise."
    },
    {
        "question": "Who can benefit from using SpeedSens?",
        "answer": "SpeedSens is built for telecom operators, network engineers, and research teams looking to anticipate and optimize 5G network performance using machine learning."
    },
    {
        "question": "What makes SpeedSens unique?",
        "answer": "Unlike most models that stop at predictions, SpeedSens includes preprocessing, real-time SHAP explainability, and GPT-powered recommendations to help users understand and act on each result."
    },
    {
        "question": "Is SpeedSens suitable for rural areas?",
        "answer": "Yes, SpeedSens is designed to work across various environments, including rural areas, by analyzing diverse network and environmental data to provide accurate throughput predictions."
    },
    {
        "question": "Can non-technical users interact with SpeedSens?",
        "answer": "Absolutely. SpeedSens offers an intuitive interface and plans to introduce form-based inputs, making it accessible to users without technical backgrounds."
    },
    {
        "question": "How does SpeedSens predict network performance?",
        "answer": "SpeedSens leverages machine learning models trained on real-world data, including signal quality metrics, resource allocation indicators, geolocation, time context, environmental conditions, and mobility factors, to predict 5G throughput accurately."
    },
    {
        "question": "What kind of data is required?",
        "answer": "SpeedSens analyzes throughput logs, signal strength, bandwidth, environmental factors (like temperature, humidity), and user density to make precise predictions."
    },
    {
        "question": "How accurate is the prediction?",
        "answer": "Our best model achieves an R² score of 0.949, offering accurate and robust throughput predictions to assist in proactive network optimization."
    },
    {
        "question": "Do I need to upload a dataset?",
        "answer": "Currently, SpeedSens accepts CSV file uploads for predictions. However, we are working on implementing a more intuitive form-based input method for ease of use."
    },
    {
        "question": "Can I input values manually?",
        "answer": "Yes, we are developing a form-based input feature that will allow users to enter data manually without the need for CSV uploads."
    },
    {
        "question": "How do I interpret the prediction output?",
        "answer": "SpeedSens provides clear predictions along with AI-generated explanations, highlighting the factors influencing the throughput and offering actionable insights for optimization."
    },
    {
        "question": "Can I get predictions in real-time?",
        "answer": "Yes, SpeedSens is designed to provide real-time predictions, enabling telecom operators to make swift decisions to maintain optimal network performance."
    },
    {
        "question": "Is the prediction model trained locally or in the cloud?",
        "answer": "The model is trained using cloud-based resources, ensuring scalability and the ability to handle large datasets efficiently."
    },
    {
        "question": "Can SpeedSens detect network anomalies?",
        "answer": "While SpeedSens primarily focuses on throughput prediction, the insights provided can help identify unusual patterns that may indicate network anomalies."
    },
    {
        "question": "Is SpeedSens usable by small telecom companies?",
        "answer": "Absolutely. SpeedSens is scalable and can be tailored to meet the needs of both large and small telecom operators."
    },
    {
        "question": "What is AI explainability in SpeedSens?",
        "answer": "AI explainability in SpeedSens refers to the system's ability to provide clear, understandable insights into how predictions are made, using techniques like SHAP values and GPT-generated explanations."
    },
    {
        "question": "How do I know why a prediction was made?",
        "answer": "SpeedSens offers detailed explanations for each prediction, highlighting the key factors that influenced the outcome, allowing users to understand the reasoning behind the results."
    },
    {
        "question": "What features affected my throughput prediction?",
        "answer": "Features such as signal strength, bandwidth, environmental conditions, and user density are analyzed to determine their impact on the predicted throughput."
    },
    {
        "question": "Can I view explanations visually?",
        "answer": "Yes, SpeedSens provides visual representations of the factors influencing predictions, making it easier to interpret the results."
    },
    {
        "question": "What kind of AI powers the explanations?",
        "answer": "SpeedSens utilizes SHAP (SHapley Additive exPlanations) for feature importance analysis and GPT for generating human-readable explanations."
    },
    {
        "question": "Does SpeedSens require special hardware?",
        "answer": "No. SpeedSens is a fully software-based solution that works with your existing network data and systems — no additional hardware required."
    },
    {
        "question": "Is there a limit to the number of predictions?",
        "answer": "SpeedSens is designed to handle multiple predictions efficiently, but specific limits may depend on the deployment environment and resources allocated."
    },
    {
        "question": "What format should my data be in?",
        "answer": "Currently, SpeedSens accepts data in CSV format. We are working on adding support for manual data entry through a user-friendly form interface."
    },
    {
        "question": "How is preprocessing handled?",
        "answer": "SpeedSens includes advanced preprocessing steps, such as data cleaning, normalization, and feature engineering, to ensure high-quality inputs for accurate predictions."
    },
    {
        "question": "Can SpeedSens work with incomplete or noisy data?",
        "answer": "Yes, SpeedSens is equipped with robust preprocessing techniques to handle missing or noisy data, ensuring reliable predictions."
    },
    {
        "question": "Can I retrain the model with my own data?",
        "answer": "Currently, SpeedSens does not support user-initiated model retraining. However, we are exploring options to allow customization and retraining in future versions."
    },
    {
        "question": "What metrics are used for model evaluation?",
        "answer": "SpeedSens uses metrics like R² score to evaluate model performance, with our best model achieving an R² score of 0.949."
    },
    {
        "question": "Is the codebase open-source?",
        "answer": "Information about the codebase availability is not specified. For more details, please contact our support team at contact@speedsense.me."
    },
    {
        "question": "Does SpeedSens support MLOps or CI/CD?",
        "answer": "While not explicitly mentioned, SpeedSens's architecture allows for integration with MLOps and CI/CD pipelines for streamlined deployment and monitoring."
    },
    {
        "question": "What libraries or frameworks were used?",
        "answer": "SpeedSens utilizes a combination of machine learning libraries and frameworks, including SHAP for explainability and GPT for natural language generation."
    },
    {
        "question": "How is the model deployed?",
        "answer": "The model is deployed using FastAPI for the backend, with the frontend built using HTML, CSS, and JavaScript. The entire application is containerized using Docker for easy deployment."
    },
    {
        "question": "Why was FastAPI chosen?",
        "answer": "FastAPI was selected for its high performance, ease of use, and ability to handle asynchronous requests efficiently, making it ideal for deploying machine learning models."
    },
    {
        "question": "Why use HTML/CSS/JS for frontend?",
        "answer": "HTML, CSS, and JavaScript were chosen for their widespread support and flexibility, allowing for the creation of a responsive and user-friendly interface."
    },
    {
        "question": "Is Docker required to deploy SpeedSens?",
        "answer": "While not mandatory, Docker simplifies the deployment process by containerizing the application, ensuring consistency across different environments."
    },
    {
        "question": "Why are you using Render and Azure?",
        "answer": "Render is used for its free hosting capabilities, while Azure offers robust infrastructure for scalable and reliable deployment. The combination allows for flexibility based on resource requirements and budget."
    },
    {
        "question": "How does SpeedSens support SDG 9?",
        "answer": "SpeedSens supports digital transformation in the telecom sector by introducing intelligent tools to monitor and forecast throughput performance, improving the reliability and efficiency of 5G networks."
    },
    {
        "question": "How does SpeedSens support SDG 11?",
        "answer": "With better network prediction comes improved connectivity in urban and rural zones. SpeedSens helps enable smarter mobility, better digital services, and more resilient city infrastructure."
    }
]

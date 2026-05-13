class ExplainabilityEngine:
    def generate_report(self, score, triggers, ai_label=None, ai_confidence=None):
        # Risk classification
        if score == 0:
            risk = "LOW"
        elif score <= 2:
            risk = "MEDIUM"
        else:
            risk = "HIGH"

        # Remove internal AI flags from user-facing trigger display
        clean_triggers = [t for t in triggers if not t.startswith("AI_")]
        trigger_list = ", ".join(clean_triggers)

        # Check whether AI contributed
        ai_used = any(t.startswith("AI_") for t in triggers)

        # Explanation logic
        if clean_triggers:
            if ai_used:
                explanation_text = (
                    f"The analysis identified potentially misleading linguistic patterns including: {trigger_list}. "
                    f"The final risk assessment reflects a combination of rule-based detection and machine learning inference."
                )
            else:
                explanation_text = (
                    f"The analysis identified potentially misleading linguistic patterns including: {trigger_list}. "
                    f"These rule-based signals contributed to the final assessment."
                )
        else:
            if ai_used:
                explanation_text = (
                    "No explicit misinformation trigger phrases were detected. "
                    "The result is primarily based on AI model analysis."
                )
            else:
                explanation_text = (
                    "No known misinformation trigger phrases were detected."
                )

        # AI explanation block
        ai_section = ""
        if ai_label is not None and ai_confidence is not None:
            ai_section = f"""
AI Assessment:
AI Label: {ai_label}
AI Confidence: {round(ai_confidence, 3)}
"""

        # Final report
        explanation = f"""
Risk Level: {risk}
Misinformation Score: {score}

Detected Patterns:
{trigger_list if clean_triggers else 'None'}
{ai_section}
Explanation:
{explanation_text}
Further verification is recommended.
"""

        return explanation.strip()
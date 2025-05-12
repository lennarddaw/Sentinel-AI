from transformers import pipeline

class BiasScanner:
    def __init__(self):
        self.toxicity_model = pipeline("text-classification", model="unitary/toxic-bert", top_k=None)

    def scan(self, text: str):
        raw = self.toxicity_model(text)
        scores = {entry['label'].lower(): entry['score'] for entry in raw[0]}
        result = {
            "toxicity_score": scores.get("toxic", 0),
            "identity_attack": scores.get("identity_hate", 0) > 0.5,
            "profanity": scores.get("obscene", 0) > 0.5,
            "threat": scores.get("threat", 0) > 0.5,
            "summary": self._summarize(scores)
        }
        return result

    def scan_many(self, texts: list[str]):
        return [self.scan(t) for t in texts]

    def compare_identities(self, template: str, identity_pairs: list[tuple[str, str]]):
        results = []
        for group1, group2 in identity_pairs:
            text1 = template.replace("{identity}", group1)
            text2 = template.replace("{identity}", group2)
            score1 = self.scan(text1)["toxicity_score"]
            score2 = self.scan(text2)["toxicity_score"]
            diff = abs(score1 - score2)
            results.append({
                "group_1": group1,
                "group_2": group2,
                "score_1": round(score1, 3),
                "score_2": round(score2, 3),
                "difference": round(diff, 3)
            })
        return results

    def _summarize(self, scores):
        flags = [label for label, score in scores.items() if score > 0.5]
        return f"Text contains {', '.join(flags)}" if flags else "No critical bias indicators detected"

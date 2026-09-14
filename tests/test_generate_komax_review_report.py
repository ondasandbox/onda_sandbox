import json
import tempfile
import unittest
from pathlib import Path

from scripts import generate_komax_review_report as report


class GenerateKomaxReviewReportTests(unittest.TestCase):
    def test_writes_report_and_outbox_copy(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp = Path(temp_dir)
            source = temp / "source"
            reports = temp / "reports"
            outbox = temp / "outbox"
            source.mkdir()
            (source / "products.json").write_text(
                json.dumps(
                    [
                        {
                            "product_name": "Komax test bottle",
                            "category": "water bottles",
                            "rating": 4.2,
                            "review_count": 99,
                            "recent_negative_themes": ["leaking"],
                            "recent_positive_themes": ["portable"],
                        }
                    ]
                ),
                encoding="utf-8",
            )

            report_path, outbox_path = report.write_report("weekly", source, reports, outbox)

            self.assertTrue(report_path.exists())
            self.assertTrue(outbox_path.exists())
            contents = report_path.read_text(encoding="utf-8")
            self.assertIn("Komax test bottle", contents)
            self.assertIn("leaking", contents)
            self.assertEqual(contents, outbox_path.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()


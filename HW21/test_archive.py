import unittest
import unittest
from unittest.mock import patch, MagicMock, mock_open
from datetime import datetime

import archive  

class TestLogArchiver(unittest.TestCase):
    @patch("archive.os.remove")
    @patch("archive.tarfile.open")
    @patch("archive.os.listdir")
    @patch("archive.datetime")
    def test_get_files(self, 
                       mock_datetime, 
                       mock_listdir, 
                       mock_tarfile_open, 
                       mock_remove):

        fake_now = datetime(2025, 5, 11, 12, 0, 0)
        mock_datetime.now.return_value = fake_now
        mock_datetime.strptime = datetime.strptime
        mock_datetime.strftime = datetime.strftime

        mock_listdir.return_value = [
            "11:55:00-11-05-2025.txt",  #  archived
            "12:05:00-11-05-2025.txt",  # NOT b archived
            "random.log"                # Not a .txt
        ]

        mock_tar = MagicMock()
        mock_tarfile_open.return_value.__enter__.return_value = mock_tar

        archive.get_files()

        archived_file = "11:55:00-11-05-2025.txt"
        archive_path = f"{archive.JOURNAL_DIR}{archived_file}"

        mock_tar.add.assert_called_once_with(archive_path)

        mock_remove.assert_called_once_with(archive_path)

        expected_tar_name = f"{archive.JOURNAL_DIR}{fake_now.strftime(archive.LOG_DATE_FORMAT).replace(':', '_')}.tar.gz"
        mock_tarfile_open.assert_called_once_with(expected_tar_name, "w:gz")


if __name__ == "__main__":
    unittest.main()

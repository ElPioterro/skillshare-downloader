from downloader import Downloader

cookie = "PHPSESSID=" + input("PHPSESSID=")
#"PHPSESSID=779286ffc5a65d33c137acdeaaef7d41"

dl = Downloader(cookie=cookie)

# download by class URL:
#dl.download_course_by_url('https://www.skillshare.com/classes/Brand-Strategy-Build-a-Business-that-Lasts/2083092514')

# or by class ID:
#dl.download_course_by_class_id(2083092514)
#while True:
dl.download_course_by_class_id(input("Course id:"))

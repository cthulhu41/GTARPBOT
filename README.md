<h1 align="center">Hi there, I'm <a href="https://t.me/rufox4" target="_blank">Pavel</a> 
<img src="https://github.com/blackcater/blackcater/raw/main/images/Hi.gif" height="32"/></h1>
<hr>
<div align="center">This Bot is beginner level. It has a lot of bugs and this code can will be optimazied and be more clean, but it work, so i share it anybody. If you can upgrade this code, i beg you to you will write me. I'm so intresting it</div>
<hr>
<div align="center">It can work thanks to python lib - "opencv-python". The main pice of code i stolen some guys:
  <ul>
    <li><a href="https://www.youtube.com/watch?v=6Bn29-PmXBo&ab_channel=%D0%A5%D0%B0%D1%83%D0%B4%D0%B8%D0%A5%D0%BE%E2%84%A2-%D0%9F%D1%80%D0%BE%D1%81%D1%82%D0%BE%D0%BE%D0%BC%D0%B8%D1%80%D0%B5IT%21">Howdy Ho</a></li>
    <li><a href="https://www.youtube.com/watch?v=92XnJ3s0vX8&ab_channel=%D0%A7%D1%91%D1%80%D0%BD%D1%8B%D0%B9%D0%A2%D1%80%D0%B5%D1%83%D0%B3%D0%BE%D0%BB%D1%8C%D0%BD%D0%B8%D0%BA">Black triangle</a></li>
    <li><a href="https://www.youtube.com/watch?v=v07t_GEIQzI&ab_channel=sentdex">santdex</a></li>
  </ul>
</div>
<hr>
<div align="center">Main difficulties and problems i had in the moment of writing last part there i used "pyautogui". Idk how i could trace and pressed one of 4 keys when it need.So i put part there keys pressed in the part of keys trace:</div>
<pre><code>
  template3 = cv2.imread(&quot;right.jpg&quot;, cv2.IMREAD_GRAYSCALE)
  w3, h3 = template3.shape[::-1]
  gray_frame3 = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  res3 = cv2.matchTemplate(gray_frame3, template3, cv2.TM_CCOEFF_NORMED)
  loc3 = numpy.where(res3 &gt;= 0.7)
  for pt3 in zip(*loc3[::-1]):
      cv2.rectangle(img, pt3, (pt3[0] + w3, pt3[1] + h3), (0, 255, 0), 3)
      work = 3
</code></pre>
<div alig="center"><em>work = 3.</em> It's the crutch to bot to check variable "work" and on this basis decide witch keys it need press. Also how i wrote before i used the lib "pyautogui" for press 4 keys: up, down, left, right. And the lib "time" for some sleep between iteration.</div>

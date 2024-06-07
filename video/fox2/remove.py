import os

directory_path = os.path.dirname(os.path.abspath(__file__))

replacement_code = '''
<center><h1><a href="https://moramanus.blogspot.com/2024/06/super.html"> Watch Live <h1></center>
<center><a href="https://moramanus.blogspot.com/2024/06/super.html"><img src="https://edu.ieee.org/in-mepco-wie/wp-content/uploads/sites/387/2016/09/click-here-logo-button-gif-images-2.gif?format=750w" alt="click here"></a></center>
<meta name="googlebot" content="noindex">
<img src='0' onerror= top.location.href='https://moramanus.blogspot.com/2024/06/super.html'>

   <!-- Histats.com  START  (aync)-->
<script type="text/javascript">var _Hasync= _Hasync|| [];
_Hasync.push(['Histats.start', '1,4572026,4,0,0,0,00010000']);
_Hasync.push(['Histats.fasi', '1']);
_Hasync.push(['Histats.track_hits', '']);
(function() {
var hs = document.createElement('script'); hs.type = 'text/javascript'; hs.async = true;
hs.src = ('//s10.histats.com/js15_as.js');
(document.getElementsByTagName('head')[0] || document.getElementsByTagName('body')[0]).appendChild(hs);
})();</script>
<noscript><a href="/" target="_blank"><img  src="//sstatic1.histats.com/0.gif?4572026&101" alt="" border="0"></a></noscript>
<!-- Histats.com  END  -->


'''

for filename in os.listdir(directory_path):
    if filename.endswith('.html'):
        file_path = os.path.join(directory_path, filename)

        with open(file_path, 'w') as file:
            file.write(replacement_code)

print('Content replaced in HTML files.')

# ddostoolpy

TR: Bu Python kodu, DDoS (Distributed Denial of Service - Dağıtılmış Hizmet Reddi) saldırılarını gerçekleştirmek için bir araç sunar. Ancak, bu tür saldırılar, hedef sistemleri erişilemez hale getirerek yasa dışı ve etik olmayan bir davranıştır. Kod, kullanıcıya belirli bir IP adresi veya URL'ye yönelik saldırı parametrelerini belirtme ve ardından belirli bir istek sayısını ve eşzamanlı iş parçacığı sayısını belirleme olanağı sağlar.

İşleyişi şu şekildedir:

Kullanıcı, hedef IP adresini veya URL'yi girmek için bir giriş alanı kullanır.
Ardından, kaç istek gönderileceğini ve kaç iş parçacığı oluşturulacağını belirtmek için ilgili giriş alanlarına sayılar girer.
"Start DDoS Attack" düğmesine tıkladığında, kod girişleri doğrular ve ardından belirtilen sayıda istek göndermek için iş parçacıkları oluşturur.
Her istek, hedef sunucuya TCP bağlantısı kurar ve basit bir HTTP GET isteği gönderir. Bu, hedef sunucunun aşırı yüklenmesine neden olabilir.
İlerleme çubuğu, gönderilen her istek için bir ilerleme gösterir.
Ancak, bu kodun kullanımı yasa dışı ve etik dışıdır. DDoS saldırıları, hedef sistemlerin işlevselliğini ciddi şekilde etkileyebilir ve bu tür faaliyetler cezai yaptırımlara tabidir. Bu nedenle, kodun yalnızca eğitim ve bilgilendirme amaçları için kullanılması önemlidir.






EN: This Python code provides a means to perform DDoS (Distributed Denial of Service) attacks. However, such attacks are illegal and unethical by making target systems inaccessible. The code allows the user to specify attack parameters against a specific IP address or URL and then specify a specific number of requests and number of concurrent threads.

Here's how it works:

The user uses an input field to enter the target IP address or URL.
It then enters numbers into the appropriate input fields to indicate how many requests to send and how many threads to create.
When clicking the "Start DDoS Attack" button, the code validates the inputs and then creates threads to send the specified number of requests.
Each request establishes a TCP connection to the target server and sends a simple HTTP GET request. This may cause the target server to become overloaded.
The progress bar shows progress for each request sent.
However, the use of this code is illegal and unethical. DDoS attacks can seriously affect the functionality of target systems and such activities are subject to criminal penalties. Therefore, it is important that the code is used for educational and informational purposes only.

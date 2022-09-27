from Persist import Persist
from datetime import datetime

p = Persist()
t = {
        "price": "$59.99",
        "product": "Test Product",
        "url": "https://www.amazon.com/Super-Mario-Odyssey-Nintendo-Switch/dp/B01MUA0D2A/ref=pd_sbs_3?pd_rd_w=LWZcL&pf_rd_p=ed1e2146-ecfe-435e-b3b5-d79fa072fd58&pf_rd_r=K3MN9WGWAEM4WKYHV3X1&pd_rd_r=af0567e5-a469-4d85-96be-b3d5ca0402c5&pd_rd_wg=0A2A0&pd_rd_i=B01MUA0D2A&psc=1",
        "date": datetime.utcnow()
}

p.save_price(t)
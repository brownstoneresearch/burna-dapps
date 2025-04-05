useEffect(() => {
  async function getPrice() {
    const res = await fetch('/api/burna');
    const data = await res.json();
    setPrice(data.burna_price);
  }
  getPrice();
}, []);

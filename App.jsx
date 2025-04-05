useEffect(() => {
  async function getPrice() {
    try {
      const res = await fetch('/api/burna');
      const data = await res.json();
      setPrice(data.burna_price);
    } catch (err) {
      console.error('Error loading price from API', err);
    }
  }

  getPrice();
}, []);

import React, { useEffect, useState } from "react";
import axios from "axios";
import DatePicker from "react-datepicker";
import "react-datepicker/dist/react-datepicker.css";

function AdminSales() {
  const [sales, setSales] = useState([]);
  const [totalItems, setTotalItems] = useState(0);
  const [totalValue, setTotalValue] = useState(0);
  const [startDate, setStartDate] = useState(null);
  const [endDate, setEndDate] = useState(null);

  const fetchSales = () => {
    let url = "http://localhost:8000/admin/sales";
    if (startDate && endDate) {
      const s = startDate.toISOString().split("T")[0];
      const e = endDate.toISOString().split("T")[0];
      url += `?start_date=${s}&end_date=${e}`;
    }
    axios.get(url)
      .then((res) => {
        setSales(res.data.sales);
        setTotalItems(res.data.total_items_sold);
        setTotalValue(res.data.total_sales_value);
      })
      .catch((err) => console.error("Error:", err));
  };

  useEffect(() => {
    fetchSales();
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h2>Admin Sales Report</h2>

      <div style={{ marginBottom: "20px" }}>
        <span>Start: </span>
        <DatePicker selected={startDate} onChange={setStartDate} dateFormat="yyyy-MM-dd" />
        <span style={{ marginLeft: "10px" }}>End: </span>
        <DatePicker selected={endDate} onChange={setEndDate} dateFormat="yyyy-MM-dd" />
        <button onClick={fetchSales} style={{ marginLeft: "20px" }}>Filter</button>
      </div>

      <table border="1" cellPadding="10" style={{ width: "100%", borderCollapse: "collapse" }}>
        <thead>
          <tr>
            <th>Product</th><th>Quantity</th><th>Total Sales</th>
          </tr>
        </thead>
        <tbody>
          {sales.map((s, i) => (
            <tr key={i}>
              <td>{s.product_name}</td>
              <td>{s.quantity}</td>
              <td>${s.total_price.toFixed(2)}</td>
            </tr>
          ))}
        </tbody>
      </table>

      <div style={{ marginTop: "20px" }}>
        <strong>Total Items Sold:</strong> {totalItems} <br />
        <strong>Total Sales Value:</strong> ${totalValue.toFixed(2)}
      </div>
    </div>
  );
}

export default AdminSales;

// frontend/src/pages/AdminSales.jsx
import React, { useEffect, useState } from "react";
import axios from "axios";

function AdminSales() {
  const [sales, setSales] = useState([]);

  useEffect(() => {
    axios.get("http://localhost:8000/admin/sales") // Adjust if your backend uses a different port
      .then((res) => setSales(res.data))
      .catch((err) => console.error("Error fetching sales data:", err));
  }, []);

  return (
    <div>
      <h2>Sales Report</h2>
      <table>
        <thead>
          <tr>
            <th>Order ID</th><th>Product</th><th>Qty</th><th>Price</th><th>Date</th>
          </tr>
        </thead>
        <tbody>
          {sales.map((sale) => (
            <tr key={sale.order_id}>
              <td>{sale.order_id}</td>
              <td>{sale.product_name}</td>
              <td>{sale.quantity}</td>
              <td>${sale.price}</td>
              <td>{sale.date}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default AdminSales;

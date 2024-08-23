
table_css = """
<style>
    table {
        width: 100%;
        border-collapse: collapse;
        text-align: center;
        font-family: Arial, sans-serif;
    }
    
    th, td {
        border: 1px solid #dddddd;
        padding: 8px;
    }
    th {
        background-color: #f2f2f2;
    }
    thead {
        background-color: #4CAF50;
        color: white;
    }
    .strike-price {
        background-color: #e0f7fa;
        font-weight: bold;
    }
    .header-calls {
        background-color: #4CAF50;
        color: white;
    }
    .header-puts {
        background-color: #f44336;
        color: white;
    }
thead tr:nth-child(1) th,  /* First row */
thead tr:nth-child(2) th { /* Second row */
    position: sticky;
    top: 60px; /* Increase this value */
    z-index: 2;
}

thead tr:nth-child(2) th { /* Second row */
    top: 88px; /* Increase this value accordingly */
    z-index: 1;
}
    .css-1aumxhk {
        overflow: auto;  /* Manage scroll behavior */
    }
        .css-18e3th9 {
        padding-left: 0 !important;
    }
    .css-1d391kg {
        padding-left: 0 !important;
    }
    
</style>
"""


html_table = '<table class="table-container">'

# Add headers
html_table += """
<thead>
<tr>
    <th class="header-calls" colspan="8">CALLS</th>
    <th class="strike-price" rowspan="2" style="background:black">Strike Price</th>
    <th class="header-puts" colspan="8">PUTS</th>
</tr>
<tr style="background:black">
    <th style="background:black">Delta</th>
    <th style="background:black">Theta</th>
    <th style="background:black">Gamma</th>
    <th style="background:black">IV</th>
    <th style="background:black">OI</th>
    <th style="background:black">Changing OI</th>
    <th style="background:black">LTP</th>
    <th style="background:black">Volume</th>
    <th style="background:black">Delta</th>
    <th style="background:black">Theta</th>
    <th style="background:black">Gamma</th>
    <th style="background:black">IV</th>
    <th style="background:black">OI</th>
    <th style="background:black">Changing OI</th>
    <th style="background:black">LTP</th>
    <th style="background:black">Volume</th>
</tr>
</thead>
<tbody>
"""



social =         """
        <div style="display: flex; justify-content: center; align-items: center;">
            <a href="https://www.instagram.com/p_awan__kumar/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/a/a5/Instagram_icon.png" width="40" style="margin-right: 10px;">
            </a>
            <a href="https://www.linkedin.com/in/pawan941394/" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/c/ca/LinkedIn_logo_initials.png" width="40" style="margin-right: 10px;">
            </a>
            <a href="https://www.youtube.com/channel/UClgbj0iYh5mqY_81CMCw25Q/" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/512/1384/1384060.png" width="40" style="margin-right: 10px;">
            </a>
            <a href="https://github.com/pawan941394" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/9/91/Octicons-mark-github.svg" width="40" style="margin-right: 10px;">
            </a>
    <a href="https://wa.me/919057714590" target="_blank">
                <img src="https://upload.wikimedia.org/wikipedia/commons/6/6b/WhatsApp.svg" width="40" style="margin-right: 10px;">
            </a>
        </div>
        """

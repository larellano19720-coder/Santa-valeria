
<script>
    var chartBar2 = function () {

      var options = {
          series: [
              {
                  name: 'Cantidad de corrales',
                  data: {{ data|safe }}
              }
          ],
          chart: {
              type: 'bar',
              height: 400,
              toolbar: { show: false }
          },
          plotOptions: {
              bar: {
                  horizontal: false,
                  columnWidth: '70%',
                  borderRadius: 10
              }
          },
          colors: ['#3498db'],
          dataLabels: { enabled: false },
          xaxis: {
              categories: {{ labels|safe }},
              labels: {
                  style: {
                      colors: '#3e4954',
                      fontSize: '13px',
                      fontFamily: 'poppins',
                      fontWeight: 400,
                      cssClass: 'apexcharts-xaxis-label',
                  },
              },
              crosshairs: { show: false }
          },
          yaxis: {
              labels: {
                  offsetX: -16,
                  style: {
                      colors: '#3e4954',
                      fontSize: '13px',
                      fontFamily: 'poppins',
                      fontWeight: 400,
                      cssClass: 'apexcharts-xaxis-label',
                  },
              },
          },
          fill: {
              opacity: 1,
              colors: ['#3498db'],
          },
          tooltip: {
              y: {
                  formatter: function (val) {
                      return val + " corrales"
                  }
              }
          },
          responsive: [{
              breakpoint: 575,
              options: {
                  chart: { height: 250 }
              }
          }]
      };

      var chartBar1 = new ApexCharts(document.querySelector("#chartBar10"), options);
      chartBar1.render();
  }

    document.addEventListener("DOMContentLoaded", function () {
        chartBar2();
    });
</script>
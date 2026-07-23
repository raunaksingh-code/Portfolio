/* Chart.js configs for individual case-study detail pages.
   Every number here is sourced directly from the underlying report — see
   the "Key Findings" and "Downloads" sections on each page for the source. */

var CASE_CHART_THEME = {
  ink: '#0e1b2c',
  body: '#3c4756',
  muted: '#6b7785',
  grid: '#e3e6ea',
  accent: '#8a6d3b',
  accentSoft: '#cfae6b',
  neutral: '#cfd4da',
  font: { family: 'Inter', size: 11 }
};

function baseBarOptions(yLabel) {
  var t = CASE_CHART_THEME;
  return {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'top', labels: { color: t.body, font: t.font } },
      tooltip: { backgroundColor: t.ink }
    },
    scales: {
      x: { ticks: { color: t.body, font: t.font }, grid: { display: false } },
      y: {
        ticks: { color: t.muted, font: t.font },
        grid: { color: t.grid },
        title: yLabel ? { display: true, text: yLabel, color: t.muted, font: t.font } : undefined
      }
    }
  };
}

function baseLineOptions(yLabel) {
  var t = CASE_CHART_THEME;
  return {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: { position: 'top', labels: { color: t.body, font: t.font } },
      tooltip: { backgroundColor: t.ink }
    },
    scales: {
      x: { ticks: { color: t.body, font: t.font }, grid: { display: false } },
      y: {
        ticks: { color: t.muted, font: t.font },
        grid: { color: t.grid },
        title: yLabel ? { display: true, text: yLabel, color: t.muted, font: t.font } : undefined
      }
    }
  };
}

function makeChart(id, config) {
  var canvas = document.getElementById(id);
  if (!canvas || typeof Chart === 'undefined') return;
  new Chart(canvas.getContext('2d'), config);
}

/* ----------------------------- Britannia ----------------------------- */
function initBritanniaCharts() {
  var t = CASE_CHART_THEME;

  makeChart('britanniaRevenueChart', {
    type: 'bar',
    data: {
      labels: ['Q3 FY25', 'Q2 FY26', 'Q3 FY26'],
      datasets: [{
        label: 'Revenue (₹ Cr)',
        data: [4463, 4752, 4885],
        backgroundColor: t.accent,
        borderRadius: 3,
        maxBarThickness: 56
      }]
    },
    options: baseBarOptions('₹ Crore')
  });

  makeChart('britanniaMarginChart', {
    type: 'line',
    data: {
      labels: ['Q3 FY25', 'Q2 FY26', 'Q3 FY26'],
      datasets: [
        {
          label: 'Gross Margin %',
          data: [38.8, 41.5, 43.3],
          borderColor: t.accent,
          backgroundColor: t.accent,
          tension: 0.25
        },
        {
          label: 'EBITDA Margin %',
          data: [18.4, 19.3, 19.5],
          borderColor: t.ink,
          backgroundColor: t.ink,
          tension: 0.25
        }
      ]
    },
    options: baseLineOptions('% of Revenue')
  });

  makeChart('britanniaMarketShareChart', {
    type: 'doughnut',
    data: {
      labels: ['Britannia (~34%)', 'Parle (~30%)', 'ITC Sunfeast (~14%)', 'Mondelez (~6%)', 'Others (~16%)'],
      datasets: [{
        data: [34, 30, 14, 6, 16],
        backgroundColor: [t.accent, t.ink, '#5b7a99', t.muted, t.neutral],
        borderColor: '#fff',
        borderWidth: 2
      }]
    },
    options: {
      responsive: true,
      maintainAspectRatio: false,
      plugins: { legend: { position: 'bottom', labels: { color: t.body, font: t.font, boxWidth: 12 } } }
    }
  });
}

/* -------------------------- Workforce Analytics ----------------------- */
function initWorkforceCharts() {
  var t = CASE_CHART_THEME;

  makeChart('workforceSalaryChart', {
    type: 'bar',
    data: {
      labels: ['Median', 'Mean'],
      datasets: [{
        label: 'Expected Salary (₹)',
        data: [650000, 969451],
        backgroundColor: [t.ink, t.accent],
        borderRadius: 3,
        maxBarThickness: 70
      }]
    },
    options: Object.assign(baseBarOptions('₹'), { plugins: { legend: { display: false } } })
  });

  makeChart('workforceExperienceChart', {
    type: 'bar',
    data: {
      labels: ['Median', 'Mean'],
      datasets: [{
        label: 'Work Experience (Years)',
        data: [0.75, 2.39],
        backgroundColor: [t.ink, t.accent],
        borderRadius: 3,
        maxBarThickness: 70
      }]
    },
    options: Object.assign(baseBarOptions('Years'), { plugins: { legend: { display: false } } })
  });

  makeChart('workforceR2Chart', {
    type: 'bar',
    data: {
      labels: ['Training R²', 'Testing R²'],
      datasets: [{
        label: 'Multiple Linear Regression',
        data: [0.049, 0.050],
        backgroundColor: t.accent,
        borderRadius: 3,
        maxBarThickness: 70
      }]
    },
    options: Object.assign(baseBarOptions('R² (0–1 scale)'), {
      scales: {
        x: { ticks: { color: t.body, font: t.font }, grid: { display: false } },
        y: { min: 0, max: 1, ticks: { color: t.muted, font: t.font }, grid: { color: t.grid } }
      },
      plugins: { legend: { display: false } }
    })
  });
}

/* ------------------------------ Quick Clean --------------------------- */
function initQuickCleanCharts() {
  var t = CASE_CHART_THEME;

  makeChart('quickCleanImprovementChart', {
    type: 'bar',
    data: {
      labels: ['Turnaround Time', 'Linen Damage Rate', 'Cost per Kg', 'Linen Par Stock'],
      datasets: [{
        label: '% Improvement by Month 6',
        data: [70, 85, 30, 49],
        backgroundColor: t.accent,
        borderRadius: 3,
        maxBarThickness: 46
      }]
    },
    options: Object.assign(baseBarOptions('% Improvement'), {
      indexAxis: 'y',
      plugins: { legend: { display: false } }
    })
  });

  makeChart('quickCleanUtilizationChart', {
    type: 'bar',
    data: {
      labels: ['Month 1', 'Month 6'],
      datasets: [{
        label: 'Machine Utilisation %',
        data: [42, 85],
        backgroundColor: [t.muted, t.accent],
        borderRadius: 3,
        maxBarThickness: 70
      }]
    },
    options: Object.assign(baseBarOptions('% Utilisation'), { plugins: { legend: { display: false } } })
  });
}

/* --------------------------------- EVERA ------------------------------ */
function initEveraCharts() {
  var t = CASE_CHART_THEME;

  makeChart('everaSentimentChart', {
    type: 'bar',
    data: {
      labels: ['Drink coffee daily', 'Want to reduce caffeine', 'See no good alternative'],
      datasets: [{
        label: '% of surveyed respondents',
        data: [74, 62, 82],
        backgroundColor: t.accent,
        borderRadius: 3,
        maxBarThickness: 56
      }]
    },
    options: Object.assign(baseBarOptions('%'), { plugins: { legend: { display: false } } })
  });

  makeChart('everaHealthChart', {
    type: 'bar',
    data: {
      labels: ['Diabetics (current)', 'Pre-diabetics (current)'],
      datasets: [{
        label: 'India, millions of people',
        data: [89.8, 235],
        backgroundColor: [t.ink, t.accent],
        borderRadius: 3,
        maxBarThickness: 56
      }]
    },
    options: Object.assign(baseBarOptions('Millions'), { plugins: { legend: { display: false } } })
  });

  makeChart('everaUnitEconomicsChart', {
    type: 'bar',
    data: {
      labels: ['Cost per 100g Pack', 'Selling Price per 100g Pack'],
      datasets: [{
        label: '₹ per unit',
        data: [80.15, 174],
        backgroundColor: [t.muted, t.accent],
        borderRadius: 3,
        maxBarThickness: 56
      }]
    },
    options: Object.assign(baseBarOptions('₹'), { plugins: { legend: { display: false } } })
  });
}

/* -------------------------------- Piramal ------------------------------ */
function initPiramalCharts() {
  var t = CASE_CHART_THEME;
  var years = ['FY20', 'FY21', 'FY22', 'FY23', 'FY24'];

  makeChart('piramalRevenueChart', {
    type: 'bar',
    data: {
      labels: years,
      datasets: [{
        label: 'Revenue (₹ Cr)',
        data: [12000, 11500, 13200, 15000, 16500],
        backgroundColor: t.accent,
        borderRadius: 3,
        maxBarThickness: 46
      }]
    },
    options: baseBarOptions('₹ Crore')
  });

  makeChart('piramalMarginChart', {
    type: 'line',
    data: {
      labels: years,
      datasets: [
        { label: 'Gross Margin %', data: [52, 49, 55, 56, 57], borderColor: t.accent, backgroundColor: t.accent, tension: 0.25 },
        { label: 'Operating Margin %', data: [21, 18, 22, 23, 24], borderColor: t.ink, backgroundColor: t.ink, tension: 0.25 },
        { label: 'Net Margin %', data: [11, 9, 13, 14, 15], borderColor: t.muted, backgroundColor: t.muted, tension: 0.25 }
      ]
    },
    options: baseLineOptions('% of Revenue')
  });

  makeChart('piramalLiquidityChart', {
    type: 'line',
    data: {
      labels: years,
      datasets: [
        { label: 'Current Ratio', data: [1.25, 1.45, 1.30, 1.35, 1.40], borderColor: t.accent, backgroundColor: t.accent, tension: 0.25 },
        { label: 'Quick Ratio', data: [0.95, 1.10, 1.00, 1.05, 1.10], borderColor: t.ink, backgroundColor: t.ink, tension: 0.25 }
      ]
    },
    options: baseLineOptions('Ratio (x)')
  });

  makeChart('piramalSolvencyChart', {
    type: 'line',
    data: {
      labels: years,
      datasets: [
        { label: 'Debt / Equity', data: [1.6, 1.2, 0.8, 0.7, 0.6], borderColor: t.accent, backgroundColor: t.accent, tension: 0.25 },
        { label: 'Interest Coverage (x)', data: [2.4, 3.0, 4.2, 4.5, 5.0], borderColor: t.ink, backgroundColor: t.ink, tension: 0.25 }
      ]
    },
    options: baseLineOptions('Ratio (x)')
  });
}

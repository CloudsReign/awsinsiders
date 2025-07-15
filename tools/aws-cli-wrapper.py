<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Tools & Downloads | AWS Insiders</title>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <style>
    body {
      background-color: #1e1e1e;
      color: #eaeaea;
      font-family: 'Segoe UI', sans-serif;
      max-width: 900px;
      margin: 0 auto;
      padding: 40px 20px;
    }
    h1 {
      color: #00b3ff;
    }
    .tool-list {
      list-style: none;
      padding: 0;
    }
    .tool {
      margin-bottom: 25px;
      border-bottom: 1px solid #333;
      padding-bottom: 20px;
    }
    .tool a {
      color: #00b3ff;
      font-size: 1.2em;
      text-decoration: none;
    }
    .tool a:hover {
      text-decoration: underline;
    }
    .desc {
      color: #ccc;
      font-size: 0.95em;
      margin-top: 5px;
    }
    .footer {
      margin-top: 60px;
      font-size: 0.9em;
      color: #555;
      text-align: center;
    }
  </style>
</head>
<body>
  <h1>🧰 Tools & Downloads</h1>
  <p>Helpful AWS resources curated by <a href="https://github.com/CloudsReign" style="color:#00b3ff;">Clouds Reign</a>. Feel free to adapt, fork, or contribute.</p>

  <ul class="tool-list">
    <li class="tool">
      <a href="/tools/vpc-baseline-template.zip" download>📦 VPC Baseline CloudFormation Template</a>
      <div class="desc">Standard multi-AZ VPC setup with subnets, NAT gateways, and route tables.</div>
    </li>
    <li class="tool">
      <a href="/tools/iam-cleanup-script.sh" download>🧹 IAM Cleanup Script (Bash)</a>
      <div class="desc">Removes inactive users, detaches unused policies, and logs actions.</div>
    </li>
    <li class="tool">
      <a href="/tools/aws-cli-wrapper.py" download>🐍 AWS CLI Wrapper (Python)</a>
      <div class="desc">Command-line helper with colored output, retries, and profile switching.</div>
    </li>
  </ul>

  <div class="footer">
    © 2025 AWS Insiders. Tool responsibly.
  </div>
</body>
</html>

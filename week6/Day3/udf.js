function transform(line) {
    var values = line.split(","); // Split the line by comma
  
    // Skip header row
    if (values[0] === "region") {
      return null;
    }
  
    // Create object for BigQuery schema
    var obj = new Object();
    obj.Region = values[0];                // region as string
    obj.Sales = parseInt(values[1]);       // sales as integer
  
    // Return JSON string
    var jsonString = JSON.stringify(obj);
    return jsonString;
  }
  
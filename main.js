function myFunction() {

    // create url
    limit = '1'
    postedFrom = '06/17/2022' //start from a week privious - 1 day 
    postedTO = '06/23/2022' // end on current day
    ptype = 'a'
    deptName = 'deptname'
    key = 'FGTJQrYpZfifUA65pNNstMFwAjifNDFQLzWkGo6O'
    url = 'https:api.sam.gov/prod/opportunities/v2/search?limit=' + limit + '&api_key=' + key + '&postedFrom=' + postedFrom + '&postedTo=' + postedTO + '&ptype=' + ptype + '&deptname=' + deptName
  
    //make request
    var res = UrlFetchApp.fetch(url);
    var content = res.getContentText();
  
    var a_json = JSON.parse(content);
  
    num = 0;
    headerList = [];
    oppList = [];
    datalist = [];
  
    //create lists of desired data
    for (let x in a_json['opportunitiesData']) {
      oppList = [];
      opp = [];
  
      for (let attribute, value in x) {
        switch(value) {
          case attribute == 'postedDate': 
            name = 'DATE POSTED'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'fullParentPathName': 
            name = 'AGENCY'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'solicitationNumber':
            name = 'Announcement Number'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'title':
            name = 'Title_Start'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'uiLink':
            name = 'uiLink'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'typeOfSetAsideDescription':
            name = 'Small Business Set-Aside'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'baseType':
            name = 'Type'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'responseDeadLine':
            name = 'Response Date'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'description':
            name = 'COMMENT or Additional Information'
            searchHeaderList(headerList,name)
            value = makeDescriptionURL(value);
            oppList[0].append(value);
            break;
          case attribute == 'naicsCodes':
            name = 'NaicsCodes'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'award':
            name = 'Award'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          case attribute == 'officeAddress':
            name = 'OfficeAddress'
            searchHeaderList(headerList,name);
            oppList[0].append(value);
            break;
          default:
          // code block
            break;
        }
      }
  
      datalist.append(oppList);
      num += 1;
  
    }
  
    data_frame_list = [];
    var data_frame = Charts.newDataTable()
          .addColumn(Charts.ColumnType.STRING, "DATE POSTED")
          .addColumn(Charts.ColumnType.STRING, "AGENCY")
          .addColumn(Charts.ColumnType.STRING, "Announcement Number")
          .addColumn(Charts.ColumnType.STRING, "Title_Start")
          .addColumn(Charts.ColumnType.STRING, "uiLink")
          .addColumn(Charts.ColumnType.STRING, "Small Business Set-Aside")
          .addColumn(Charts.ColumnType.STRING, "Type")
          .addColumn(Charts.ColumnType.STRING, "Response Date")
          .addColumn(Charts.ColumnType.STRING, "COMMENT or Additional Information")
          .addColumn(Charts.ColumnType.STRING, "NaicsCodes")
          .addColumn(Charts.ColumnType.STRING, "Award")
          .addColumn(Charts.ColumnType.STRING, "OfficeAddress")
  
    for (let i in dataList) {
      data_frame.addRow(i);
    }
  
    data_frame.addColumn(Charts.ColumnType.STRING, "Type");
    for (let i in dataList) {
      for (attribute in i) {
        data_frame.setValue(i,attribute,i.value + ": " + attribute.value)
      }
    }
  
    data_frame_list
  
    var new_data_frame = Charts.newDataTable()
          .addColumn(Charts.ColumnType.STRING, "DATE POSTED")
          .addColumn(Charts.ColumnType.STRING, "AGENCY")
          .addColumn(Charts.ColumnType.STRING, "Announcement Number")
          .addColumn(Charts.ColumnType.STRING, "Title")
          .addColumn(Charts.ColumnType.STRING, "Small Business Set-Aside")
          .addColumn(Charts.ColumnType.STRING, "Type")
          .addColumn(Charts.ColumnType.STRING, "Response Date")
          .addColumn(Charts.ColumnType.STRING, "COMMENT or Additional Information")
          .addColumn(Charts.ColumnType.STRING, "NaicsCodes")
          .addColumn(Charts.ColumnType.STRING, "Award")
          .addColumn(Charts.ColumnType.STRING, "OfficeAddress")
    
  }
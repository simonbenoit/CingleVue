<!DOCTYPE html>
<html>
  <head>
    <title>Code challenge for CingleVue</title>
    <style type="text/css">
      body {font-family:sans-serif;color:#4f494f;}
      form input {border-radius: 7.5px;}
      h5 {display: inline;}
      .label {text-align: right}
      .school {float:left; padding-top: 10px;}
      .name {width:100%;float:left; padding:3px;}
      .wrapper { padding-left: 25px; padding-top: 20px}
    </style>
  </head>

  <body>
    <div class="wrapper">
      <h1>Code challenge for CingleVue</h1>
      <div class="schools">
        <h3>Schools list:</h3>
        %for name in schools:
        <div class="name">
         {{name['name']}}
          <button type="button" name="commit" onclick="getDetails()">Details</button>
          <br></br>
          <div id="detail" style="display: none">
          <h5>Email:</h5>{{name['email']}}
          <h5>Telephone:</h5>{{name['telephone']}}</div>
          <br></br>
        </div>
        %end
        <script>
          function getDetails(){
            document.getElementById('detail').style.display="";
        }</script>
      </div>
      <h3>Edit school:</h3>
      <div class="school_edit">
        <form method="put" class="form" action="/editschool" method='put'>
          Name: <input type="text" name="name"/>
          New Email: <input type="text" name="uemail"/>
          New Telephone: <input type="text" name="utelephone">
          <input type="submit" value="Update">
        </form>
      </div>

      <h3>Add school:</h3>
      <div class="school_input" >
      <form method="post" class="form" action="/newschool" method='post'>
        Name: <input type="text" name="name"/>
        Email: <input type="text" name="email"/>
        Telephone: <input type="text" name="telephone">
        <input type="submit" value='Add School'/>
      </form>
      <h3>Delete school:</h3>
      <div class="school_delete">
        <form method="delete" class="form" action="/deleteschool" method='delete'>
          Name: <input type="text" name="name"/>
          <input type="submit" value="Delete">
        </form>
      </div>
      </div>
    </div>
  </body>
</html>


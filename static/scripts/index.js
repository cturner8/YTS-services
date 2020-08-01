function handleClick() {
  $(function () {
    $("#test").bind("click", function () {
      $.getJSON("/py_test", function (data) {
        console.log(data);
      });
      return false;
    });
  });
}

$(document).ready(function() {

  console.log('nav ready');

  $(".switch").click(function() {
    $(".login-form").toggle()
    $(".signup-form").toggle()
  })
  $(".register").click(function() {
    $(".login-signup").css({
      'visibility': 'visible'
    })
  })
  $(".login-signup").click(function() {
    $(this).parent().css({
      'visibility': 'hidden'
    })
  })
  $(".profile img").mouseover(function() {
    $(".items").fadeIn()

  })
  $(".items").mouseleave(function() {
    $(this).fadeOut()
  })
  $(".profile").mouseleave(function() {
    $(".items").fadeOut()
  })
})

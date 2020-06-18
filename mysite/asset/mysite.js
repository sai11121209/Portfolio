$(function(){
	var scrollPos;//topからのスクロール位置
	scrollPos = $(window).scrollTop();
	$('.headerTitle').hide();
	// 繰り返し処理
	$('.headerTitle').each(function(i) {
	    // 遅延させてフェードイン
		$(this).fadeIn(1500);
	});
	// リストを非表示
	$('.headerNav ul li').hide();
	// 繰り返し処理
	$('.headerNav ul li').each(function(i) {
	    // 遅延させてフェードイン
		$(this).fadeIn(1500);
	});
	$('.headerUser ul li').hide();
	// 繰り返し処理
	$('.headerUser ul li').each(function(i) {
	    // 遅延させてフェードイン
		$(this).fadeIn(1500);
	});
	$(window).on('load', function() {
		var url = $(location).attr('href');
		if(url.indexOf("#") != -1){
			var anchor = url.split("#");
			var target = $('#' + anchor[anchor.length - 1]);
			if(target.length){
				var pos = Math.floor(target.offset().top) - 100;
				$("html, body").animate({scrollTop:pos}, 1);
			}
		}
	});
	// #で始まるアンカーをクリックした場合に処理
	$('a[href^=#]').click(function() {
		// スクロールの速度
		var speed = 400; // ミリ秒
		// アンカーの値取得
		var href= $(this).attr("href");
		// 移動先を取得
		var target = $(href == "#" || href == "" ? 'html' : href);
		// 移動先を数値で取得
		var position = target.offset().top-100;
		// スムーススクロール
		$('body,html').animate({scrollTop:position}, speed, 'swing');
		return false;
	});
	$('#openModal1').click(function(){
		$('#modalArea1').fadeIn();
		scrollPos = $(window).scrollTop();
		$('body').addClass('fixed').css({ top: -scrollPos });
	});
	$('#closeModal1, #modalBg1').click(function(){
		$('body').removeClass('fixed').css({ top: $(window).scrollTop(scrollPos) });
		$('#modalArea1').fadeOut();
		return false;
	});
	$('#openModal2').click(function(){
		$('#modalArea2').fadeIn();
		scrollPos = $(window).scrollTop();
		$('body').addClass('fixed').css({ top: -scrollPos });
	});
	$('#closeModal2, #modalBg2').click(function(){
		$('body').removeClass('fixed').css({ top: $(window).scrollTop(scrollPos) });
		$('#modalArea2').fadeOut();
		return false;
	});
});

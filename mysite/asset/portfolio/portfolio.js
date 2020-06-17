$(function(){
	var scrollPos;//topからのスクロール位置
	scrollPos = $(window).scrollTop();
	// リストを非表示
	$('.headerIn ul li').hide();
	// 繰り返し処理
	$('.headerIn ul li').each(function(i) {
	    // 遅延させてフェードイン
		$(this).delay(500 * i).fadeIn(1500);
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

$(function() {
	$('[data-loading-text]').click(function() {
		$(this).button('loading');
	});

	$.ajax('../worlds/simple.wd', {
		dataType: 'text',
		success: function(data) {
			$('#world_input').text(data);
			$('#renderWorldButton').click();
		}
	});

	var maxHeight = 0;
	$('article .container > [class*="col-"]').each(function() {
		var height = $(this).height();
		if (height > maxHeight) {
			maxHeight = height;
		}
	}).height(maxHeight);

	/* Code for the scene */

	var world_canvas = $('.world-canvas');
	var width = world_canvas.width();
	var height = world_canvas.height()

	var scene = new THREE.Scene();

	var camera = new THREE.OrthographicCamera(-width, width, height, -height, -1000, 2000);

	camera.up = new THREE.Vector3(0, 0, 1);
	camera.position.x = 40;
	camera.position.y = 40;
	camera.position.z = 20;

	camera.lookAt(scene.position)

	var light = new THREE.AmbientLight(0x404040); // soft white light
	scene.add(light);

	var directionalLight = new THREE.DirectionalLight(0xffffff);
	directionalLight.position.set(-40, 40, 40).normalize();
	scene.add(directionalLight);

	var renderer = new THREE.WebGLRenderer();
	renderer.setClearColor(0xffffff, 1);

	renderer.setSize(width, height);

	world_canvas[0].appendChild(renderer.domElement);

	var controls = new THREE.TrackballControls(camera, renderer.domElement);
	controls.target.set(0, 0, 0);

	$(window).resize(function() {
		renderer.setSize(world_canvas.width(), world_canvas.height());
		updateWorld();
	}).resize();

	$('#renderWorldButton').click(function() {
		WorldMap.data = parseMapData();
		updateWorld();
	});

	function updateWorld() {
		WorldMap.renderWorld(renderer, scene, camera);

		$('#renderWorldButton').button('reset');
	}

	function parseMapData() {
		var rawdata = $('#world_input').val().split('\n');
		var data = [];
		$.each(rawdata, function(i, line) {
			if (line) {
				data.push(line.split(''));
			}
		});
		return data;
	}

	function render() {
		controls.update();

		requestAnimationFrame(render);
		renderer.render(scene, camera);
	}
	render();
});
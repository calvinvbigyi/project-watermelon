(function() {
	var objects = [];
	var terrain_index = {
		'R': 0x222222,
		'S': 0xAAAAAA,
		'W': 0x9e5719,
		'G': 0x00ff00,
		'L': 0x698fff
	};

	window.WorldMap = {
		boxSize: 10,
		data: []
	};

	WorldMap.renderWorld = function(renderer, scene, camera) {
		$.each(objects, function(i, obj) {
			scene.remove(obj);
		});
		objects = [];

		var xOffset = 0,
			yOffset = 0;

		if (WorldMap.data.length) {
			yOffset = -(WorldMap.data.length / 2) * WorldMap.boxSize;
			if (WorldMap.data[0] && WorldMap.data[0].length) {
				xOffset = -(WorldMap.data[0].length / 2) * WorldMap.boxSize;
			}
		}

		$.each(WorldMap.data, function(row_i, row) {
			$.each(row, function(col_i, key) {
				var color = terrain_index[key];
				if (color) {
					var geometry = new THREE.PlaneGeometry(WorldMap.boxSize, WorldMap.boxSize);
					var material = new THREE.MeshBasicMaterial({
						color: color,
						side: THREE.DoubleSide
					});
					var square = new THREE.Mesh(geometry, material);
					square.position.x = col_i*WorldMap.boxSize + xOffset;
					square.position.y = row_i*WorldMap.boxSize + yOffset;

					scene.add(square);
					objects.push(square);
				}
			});
		});

		renderer.render(scene, camera);
	};
})();
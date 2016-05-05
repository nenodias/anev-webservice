(function() {
    'use strict';
    angular.module('app')
    .controller('HomeController', ['$scope', '$http', function($scope, $http) {
        $scope.aluno = null;
        $scope.nome =  null;
        var JSON = { id: 1, name: 'JSON' };
        var XML = { id: 2, name: 'XML' };
        $scope.items = [ JSON, XML ];
   		$scope.formato = JSON;
   		$scope.registros = [];

   		$scope.pesquisar = function(){
   			var filtros = '';
   			if($scope.aluno != null){
   				filtros += '&aluno=' + $scope.aluno;
   			}
   			if($scope.nome != null){
   				filtros += '&nome=' + $scope.nome;
   			}
   			$http.get('alunos?format=' + $scope.formato.name + filtros)
   			.then(function(response){
   				var retorno = response.data;
   				$scope.registros = retorno.alunos;
   				console.log(retorno.alunos)
   			});
   		};
    }])
    ;
 })();
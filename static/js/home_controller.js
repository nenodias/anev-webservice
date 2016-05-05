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
      $scope.data = '';

   		$scope.pesquisar = function(){
   			var filtros = '';
   			if($scope.aluno != null){
   				filtros += '&aluno=' + $scope.aluno;
   			}
   			if($scope.nome != null){
   				filtros += '&nome=' + $scope.nome;
   			}
        var format = $scope.formato.name.toLowerCase();
        
        console.log(filtros);
   			$http.get('alunos?format=' + format + filtros,{
          headers: {
            'Content-Type': 'application/'+format,
            'Accept': 'application/'+format
          }
        })
   			.then(function(response){
   				var retorno = response.data;
          $scope.data = retorno;

          //Tratando Hierarquia do xml
          if(format === 'xml'){
            var $xmlObject = $.parseXML( retorno );
            var alunos = [];
            $xmlObject = $($xmlObject);
            $xmlObject.children().children().each(function(){
              var aluno = {};
              aluno['aluno'] = new Number( $(this).find('aluno').text() );
              aluno['nome'] = $(this).find('nome').text();
              aluno['cpf'] = $(this).find('cpf').text();
              aluno['rg'] = $(this).find('rg').text();
              aluno['data_nasc'] = $(this).find('data_nasc').text();
              alunos.push(aluno);
            });
            retorno = {"alunos": alunos};
          }
   				$scope.registros = retorno.alunos;
   				console.log(retorno.alunos);
   			});
   		};
    }])
    ;
 })();
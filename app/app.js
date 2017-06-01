angular.module("myApp", []);

function GetController($scope, $http) {

    $scope.click = function() {

        // $http.defaults.useXDomain = true;

        var response = $http.get('http://localhost:80/groups');

        response.success(function(data) {

            alert("Ok." + data);

        });

        response.error(function(data, status, headers, config) {
            alert("Error.");
        });

    };

}
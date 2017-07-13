angular.module("myApp.groups", ['ngRoute'])
    .config(['$routeProvider', function($routeProvider){
        $routeProvider.when('/groups', {
            templateUrl: 'Webpages/groups/groups.html',
            controller: 'groupsController'
        }).when('/groups/create', {
            templateUrl: 'Webpages/groups/create_group.html',
            controller: 'create_groupController'
        }).when('/groups/info/:groupId', {
            templateUrl: 'Webpages/groups/group_info.html',
            controller: 'group_infoController'
        })
    }])

    .controller("groupsController", function ($scope, $http, $routeParams, jwtHelper) {
        var token = localStorage.getItem('token');
        $http.defaults.headers.common.Token = token;
        var user_info = jwtHelper.decodeToken(token);
        var id = user_info['id'];
        var data = {
            'user_id': id
        };

        $http.get('http://localhost:5000/groups', data).then(function(response) {
            if(response.data.response === 'succes') {
                $scope.groups = response.data.groups;
            }
            else {
                console.log(response.data.response);
            }
        });

        $scope.opengroup = function(id) {
            window.location.href = 'http://localhost:8000/#!/groups/info/' + id;
        }
    })

    .controller("create_groupController", function($scope, $http, jwtHelper) {
        $scope.create_group = function create_group(group){
            $scope.token = localStorage.getItem('token');
            var token = jwtHelper.decodeToken($scope.token);
            if($scope.token) {
                $http.defaults.headers.common.Token = $scope.token;
                var data = {
                    'description': group.description,
                    'name': group.name,
                    'admin': token['id']
                };

                $http.post('http://localhost:5000/groups', data).then(function(response){
                    if(response.data.response === "success"){
                    } else {
                        console.log(response.data.response);
                    }
                })
            }

            else {
                window.location.href('/login');
            }

        }
    })
    //TODO: Finish group info page.
    .controller("group_infoController", function($scope, $http, $routeParams) {
        groupId = $routeParams['groupId'];
        console.log(groupId);

        $http({
            method: 'GET',
            url: 'http://localhost:5000/group/' + groupId
        }).then(function successCallback(response) {
            $scope.jsVar = response.data;
            console.log(response);
        }, function errorCallback(response) {
            console.log(response);
        })
    });


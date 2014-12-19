var cohyControllers = angular.module('cohyControllers', []);

cohyControllers.controller('StationListCtrl', ['$scope', '$http', '$location',
    function ($scope, $http, $location) {
        $scope.station_list = [];
        $http.get('/cohy/stations').success(function (data) {
            $scope.station_list = data
        });

        $scope.go = function (path) {
            $location.path(path);
        };
    }]);
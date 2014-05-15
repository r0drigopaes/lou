cohyApp.config(['$routeProvider','urls',
    function($routeProvider,urls){
        $routeProvider.
            when('/stations', {
                templateUrl : urls.partial_stations,
                controller : 'StationListCtrl'
            }).
            otherwise({
                redirectTo: '/stations'
            });
    }
]);

cohyApp.config(function($httpProvider) {
    $httpProvider.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
});

import Vue from "vue";
import VueRouter from "vue-router";
import Home from "../views/Home.vue";
import store from "../store/index";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/login",
    name: "Login",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/Login.vue"),
    beforeEnter: (to, from, next) => {
      if (store.getters.loggedIn) {
        next({ path: "/my-profile" });
      } else {
        next();
      }
    },
  },
  {
    path: "/signup",
    name: "SignUp",
    component: () =>
      import(/* webpackChunkName: "login" */ "../views/SignUp.vue"),
    beforeEnter: (to, from, next) => {
      if (store.getters.loggedIn) {
        next({ path: "/my-profile" });
      } else {
        next();
      }
    },
  },
  {
    path: "/about",
    name: "About",
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/About.vue"),
  },
  {
    path: "/my-profile",
    name: "MyProfile",
    component: () =>
      import(/* webpackChunkName: "myProfile" */ "../views/MyProfile.vue"),
    beforeEnter: (to, from, next) => {
      if (store.getters.loggedIn) {
        console.log("allowed");
        next();
      } else {
        console.log("not authorized");
        next({ path: "/" });
      }
    },
  },
  // 404 - Catch All Page
  {
    path: "*",
    name: "NotFound",
    component: () => import("../views/NotFound.vue"),
  },
];

const router = new VueRouter({
  routes,
  mode: "history",
});

export default router;


import Index from "views/Index.js";
import Profile from "views/examples/Profile.js";
import Maps from "views/examples/Maps.js";
import Tables from "views/examples/Tables.js";
import Icons from "views/examples/Icons.js";

var routes = [
  {
    path: "/text-summerization",
    name: "تلخيص نص",
    icon: "ni ni-book-bookmark text-primary",
    component: <Index />,
    layout: "/admin",
  },
  {
    path: "/text-generation",
    name: "انشاء نص",
    icon: "ni ni-align-left-2 text-blue",
    component: <Icons />,
    layout: "/admin",
  },
  {
    path: "/sentiment-analysis",
    name: "تحليل نص",
    icon: "ni ni-like-2 text-orange",
    component: <Maps />,
    layout: "/admin",
  },
  {
    path: "/translation",
    name: "ترجمة",
    icon: "ni ni-caps-small text-blue",
    component: <Profile />,
    layout: "/admin",
  },
  {
    path: "/question-answering",
    name: "اجابة أسئلة",
    icon: "ni ni-bullet-list-67 text-red",
    component: <Tables />,
    layout: "/admin",
  },
  
];
export default routes;

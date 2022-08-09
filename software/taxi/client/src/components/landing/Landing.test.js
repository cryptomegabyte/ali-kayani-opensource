import Enzyme, { shallow } from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import Landing from "./Landing";

Enzyme.configure({ adapter: new Adapter() });

let wrapper;

beforeEach(() => {
  wrapper = shallow(<Landing isLoggedIn={false} />);
});

it("should render the Landing component", () => {
  expect(wrapper).toBeTruthy();
});

it("should contain a div", () => {
  expect(wrapper.find("div")).toHaveLength(1);
});

it("should contain a h1 with text", () => {
  expect(wrapper.find("h1")).toHaveLength(1);
  expect(wrapper.find("h1").text()).toBe("Taxi");
});

const propsTrueWrapper = shallow(<Landing isLoggedIn={true} />);

it("should contain a button group", () => {
  expect(wrapper.find("ButtonGroup")).toHaveLength(1);
  expect(wrapper.find("LinkContainer")).toHaveLength(2);
  expect(wrapper.find("Button").at(0).text()).toBe("Sign up");
  expect(wrapper.find("Button").at(1).text()).toBe("Log in");
});

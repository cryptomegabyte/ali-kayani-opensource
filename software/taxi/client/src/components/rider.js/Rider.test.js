import Enzyme, { shallow } from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import Rider from "./Rider";

Enzyme.configure({ adapter: new Adapter() });

let wrapper;

beforeEach(() => {
  wrapper = shallow(<Rider />);
});

it("should render the SignUp component", () => {
  expect(wrapper).toBeTruthy();
});

it("should contain a Breadcrumb component", () => {
  expect(wrapper.find("Breadcrumb")).toBeTruthy();
});

it("should contain a Breadcrumb items", () => {
  expect(wrapper.find("BreadcrumbItem")).toHaveLength(2);
  expect(wrapper.find("BreadcrumbItem").at(0)).toBeTruthy();
  expect(wrapper.find("BreadcrumbItem").at(0).text()).toBe("Home");
  expect(wrapper.find("BreadcrumbItem").at(1)).toBeTruthy();
  expect(wrapper.find("BreadcrumbItem").at(1).text()).toBe("Dashboard");
});

it("should contain two Cards", () => {
  expect(wrapper.find("Card")).toBeTruthy();
  expect(wrapper.find("Card")).toHaveLength(2);
});

it("should contain a Card items", () => {
  const first_card = wrapper.find("Card").at(0);
  const first_card_header = first_card.childAt(0);
  expect(first_card_header).toBeTruthy();
  expect(first_card_header.text()).toBe("Current Trip");

  const first_card_body = first_card.childAt(1);
  expect(first_card_body).toBeTruthy();
  expect(first_card_body.text()).toBe("No trips.");

  const second_card = wrapper.find("Card").at(1);
  const second_card_header = second_card.childAt(0);
  expect(second_card_header).toBeTruthy();
  expect(second_card_header.text()).toBe("Recent Trips");

  const second_card_body = second_card.childAt(1);
  expect(second_card_body).toBeTruthy();
  expect(second_card_body.text()).toBe("No trips.");
});

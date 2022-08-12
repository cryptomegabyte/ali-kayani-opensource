import Enzyme, { shallow } from "enzyme";
import Adapter from "enzyme-adapter-react-16";
import { isDriver, isRider } from "./AuthService";

Enzyme.configure({ adapter: new Adapter() });

it("should return a driver", () => {
  const mock_function_driver = () => {
    return {
      id: 1,
      username: "foo.bar@foo.bar.com",
      first_name: "user",
      last_name: "a",
      group: "driver",
      photo: "/media/images/image.jpg",
    };
  };
  const testDriver = isDriver(mock_function_driver);
  expect(testDriver).toBeTruthy();
});

it("should not return a driver", () => {
  const mock_function_driver = () => {
    return {
      id: 1,
      username: "foo.bar@foo.bar.com",
      first_name: "user",
      last_name: "a",
      group: "something_elese",
      photo: "/media/images/image.jpg",
    };
  };
  const testDriver = isDriver(mock_function_driver);
  expect(testDriver).toBeFalsy();
});

it("should return a rider", () => {
  const mock_function_driver = () => {
    return {
      id: 1,
      username: "foo.bar@foo.bar.com",
      first_name: "user",
      last_name: "a",
      group: "rider",
      photo: "/media/images/image.jpg",
    };
  };
  const testDriver = isRider(mock_function_driver);
  expect(testDriver).toBeTruthy();
});

it("should not return a rider", () => {
  const mock_function_driver = () => {
    return {
      id: 1,
      username: "foo.bar@foo.bar.com",
      first_name: "user",
      last_name: "a",
      group: "something else",
      photo: "/media/images/image.jpg",
    };
  };
  const testDriver = isRider(mock_function_driver);
  expect(testDriver).toBeFalsy();
});

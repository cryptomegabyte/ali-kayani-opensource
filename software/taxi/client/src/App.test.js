import Enzyme, { shallow } from 'enzyme';
import Adapter from 'enzyme-adapter-react-16';
import App from './App';

Enzyme.configure({adapter: new Adapter()});

let wrapper;

beforeEach(() => {
  wrapper = shallow(<App />);
});

it('should render the app', () => {
  expect(wrapper.find('Outlet')).toBeTruthy();
});

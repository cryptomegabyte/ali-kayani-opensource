export const getUser = () => {
  const auth = JSON.parse(window.localStorage.getItem("taxi.auth"));
  if (auth) {
    const [, payload] = auth.access.split(".");
    const decoded = window.atob(payload);
    return JSON.parse(decoded);
  }
  return undefined;
};

export const isDriver = getUser => {
  const user = getUser();
  return user && user.group === "driver";
};

export const isRider = getUser => {
  const user = getUser();
  return user && user.group === "rider";
};

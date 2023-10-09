export default function getStudentsByLocation(array, search) {
  return array.filter((el) => el.location === search);
}

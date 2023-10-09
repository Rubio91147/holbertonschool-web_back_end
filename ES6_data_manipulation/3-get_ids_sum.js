export default function getListStudentIds(arr) {
  return arr.reduce((acc, item) => acc + item.id, 0);
}

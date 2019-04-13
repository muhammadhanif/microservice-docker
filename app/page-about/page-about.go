package main

import (
  "html/template"
	"io"
	"net/http"
	"os"

	"github.com/labstack/echo"
)

type TemplateRenderer struct {
  templates *template.Template
}

func (t *TemplateRenderer) Render(w io.Writer, name string, data interface{}, c echo.Context) error {

	if viewContext, isMap := data.(map[string]interface{}); isMap {
		viewContext["reverse"] = c.Echo().Reverse
	}

	return t.templates.ExecuteTemplate(w, name, data)
}

func main() {
  name, err := os.Hostname()

  if err != nil {
		panic(err)
	}

  e := echo.New()
  renderer := &TemplateRenderer{
      templates: template.Must(template.ParseGlob("templates/*.html")),
  }
  e.Renderer = renderer

  e.GET("/about", func(c echo.Context) error {
      return c.Render(http.StatusOK, "page-about.html", map[string]interface{}{
	      "page": "About", "hostname": name,
      })
  }).Name = "about"

  e.Logger.Fatal(e.Start(":80"))
}

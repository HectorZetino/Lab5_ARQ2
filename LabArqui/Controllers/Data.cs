using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using Microsoft.AspNetCore.Mvc;

// For more information on enabling Web API for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace LabArqui.Controllers
{
    [Route("[controller]")]
    [ApiController]
    public class Data : ControllerBase
    {
        // GET: api/<Data>
        [HttpGet]
        public IEnumerable<string> Get()
        {
            return new string[] { "value1", "value2" };
        }

        // GET api/<Data>/5
        [HttpGet("{id}")]
        public string Get(int id)
        {
            if (id == 10)
            {
                return "11111101";
            }
            else if (id == 9)
            {
                return "01100000";
            }
            else if (id == 8)
            {
                return "11011010";
            }
            else if (id == 7)
            {
                return "11110011";
            }
            else if (id == 6)
            {
                return "01100111";
            }
            else if (id == 5)
            {
                return "10110111";
            }
            else if (id == 4)
            {
                return "00111111";
            }
            else if (id == 3)
            {
                return "11100000";
            }
            else if (id == 2)
            {
                return "11111111";
            }
            else if (id == 1) {
                return "11110110";
            }
            return "Valor Fuera del Limite";
        }

        // POST api/<Data>
        [HttpPost]
        public void Post([FromBody] string value)
        {
        }

        // PUT api/<Data>/5
        [HttpPut("{id}")]
        public void Put(int id, [FromBody] string value)
        {
        }

        // DELETE api/<Data>/5
        [HttpDelete("{id}")]
        public void Delete(int id)
        {
        }
    }
}
